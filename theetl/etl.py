import yaml
import importlib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ETL:
    def __init__(self, config_path, config_name):
        configs = self.read_yaml(config_path)
        if configs:
            config = next((item for item in configs if item.get('name') == config_name), None)
            if config:
                self.loads, self.load_names = self.load_module_functions(config.get('loads', []))
                self.transformations, self.transformation_names = self.load_module_functions(config.get('transformations', []))
                self.filters, self.filter_names = self.load_module_functions(config.get('filters', []))
                self.extraction, self.extraction_name = self.load_module_function(config.get('extraction'))
            else:
                logger.error(f"No configuration found with the name: {config_name}")
        else:
            logger.error("No configurations loaded from the file.")

    @staticmethod
    def read_yaml(path):
        try:
            with open(path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            logger.error(f"The file was not found at path: {path}")
            return []

    def load_module_function(self, module_function_str):
        if module_function_str:
            try:
                module_name, function_name = module_function_str.rsplit('.', 1)
                module = importlib.import_module(module_name)
                func = getattr(module, function_name)
                return func, function_name
            except ImportError as e:
                logger.error(f"Error importing module: {e}")
                return None, None
            except AttributeError as e:
                logger.error(f"Error accessing attribute: {e}")
                return None, None
        return None, None

    def load_module_functions(self, module_functions_list):
        functions = []
        function_names = []
        for func_str in module_functions_list:
            func, name = self.load_module_function(func_str)
            if func:
                functions.append(func)
                function_names.append(name)
        return functions, function_names

    def get_function_names(self, function_type):
        return getattr(self, f"{function_type}_names", [])
