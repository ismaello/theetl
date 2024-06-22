from theetl.etl import ETL

def main():
    etl_instance = ETL('config/etl-example.yaml',"example2")
    
    # Ejecutando la función de extracción si está disponible
    if etl_instance.extraction:
        etl_instance.extraction("hola")
    
    # Ejecutando las transformaciones
    for transformation in etl_instance.transformations:
        transformation("hola")
    
    # Ejecutando las cargas
    for load in etl_instance.loads:
        load("hola")
    
    # Imprimiendo los nombres de las funciones cargadas
    print("Nombres de las funciones de carga (loads):", etl_instance.get_function_names('load'))
    print("Nombres de las funciones de transformación:", etl_instance.get_function_names('transformation'))
    print("Nombres de las funciones de filtro:", etl_instance.get_function_names('filter'))
    print("Nombre de la función de extracción:", etl_instance.extraction_name)

if __name__ == "__main__":
    main()
