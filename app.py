from theetl.etl import ETL

def main():
    etl_instance = ETL('config/etl-example.yaml',"example2")
    
    if etl_instance.extraction:
        etl_instance.extraction("hola")
    
    
    for transformation in etl_instance.transformations:
        transformation("hola")
    
    
    for load in etl_instance.loads:
        load("hola")
    
    # Imprimiendo los nombres de las funciones cargadas
    print("Loads:", etl_instance.get_function_names('load'))
    print("Transformacions:", etl_instance.get_function_names('transformation'))
    print("Filters:", etl_instance.get_function_names('filter'))
    print("Extraction:", etl_instance.extraction_name)

if __name__ == "__main__":
    main()
