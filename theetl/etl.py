import yaml
import importlib
import logging

# Configura el logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ETL:
    def __init__(self, config_path):
        self.config = self.read_yaml(config_path)
        self.loads, self.load_names = self.load_module_functions(self.config.get('loads', []))
        self.transformations, self.transformation_names = self.load_module_functions(self.config.get('transformations', []))
        self.filters, self.filter_names = self.load_module_functions(self.config.get('filters', []))
        self.extraction, self.extraction_name = self.load_module_function(self.config.get('extraction'))

    @staticmethod
    def read_yaml(path):
        """Reads a YAML file from the given path and returns the content as a dictionary."""
        try:
            with open(path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            logger.error("The file was not found at path: %s", path)
            return None

    def load_module_function(self, module_function_str):
        """Attempts to dynamically load a module and retrieve a function by its name."""
        if module_function_str:
            try:
                module_name, function_name = module_function_str.rsplit('.', 1)
                module = importlib.import_module(module_name)
                func = getattr(module, function_name)
                return func, function_name
            except ImportError as e:
                logger.error("Error importing module: %s", e)
                return None, None
            except AttributeError as e:
                logger.error("Error accessing attribute: %s", e)
                return None, None
        return None, None

    def load_module_functions(self, module_functions_list):
        """Loads multiple module functions given a list of module.function strings."""
        functions = []
        function_names = []

        # Verificar si la lista de funciones es None o está vacía
        if module_functions_list is None:
            return functions, function_names

        for func_str in module_functions_list:
            func, name = self.load_module_function(func_str)
            if func:
                functions.append(func)
                function_names.append(name)
        return functions, function_names


    def get_function_names(self, function_type):
        """Returns a list of names for the loaded functions of a given type."""
        return getattr(self, f"{function_type}_names", [])
