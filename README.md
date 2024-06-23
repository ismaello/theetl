# TheETL Project

## Description

TheETL is a Python module designed to facilitate and automate Extract, Transform, Load (ETL) processes. This tool allows users to define ETL configurations in a YAML file, which can then be executed to process and manipulate data efficiently and systematically.

## Features

- **YAML-based Configuration**: Define your ETL processes with flexible, easy-to-understand configurations.
- **Support for Multiple Configurations**: Load and execute different ETL configurations specified by name, allowing multiple workflows in a single project.
- **Extensibility**: Easily expandable with new features and adaptable to various environments and use cases.

## Requirements

TheETL requires Python 3.6 or newer. Specific Python dependencies are listed in the `requirements.txt` file, which includes:

- `pyyaml`
- `importlib`

## Installation

Clone this repository to your local machine using:

```bash
git clone https://your-repository/theetl.git
```

To install dependencies, navigate to the project directory and run:
    
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To use TheETL in your project, first, you must create an appropriate YAML configuration file. Here is a basic example of how to structure this file:
    
    ```yaml
    - name: example
  extraction: etl.extraction.avro.load_avro
  transformations:
    - etl.transformation.processing.process_data
  filters:
    - etl.filters.filters.unique_ids
  loads:
    - etl.load.big_query.big_query
    - etl.load.pub_sub.pub_sub
    ```

To load and execute an ETL configuration:
    
    ```python
    from etl.etl import ETL
    etl_instance = ETL('path_to_your_config.yaml', 'example')
    ``` 