import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    This code defines a function read_yaml that reads a YAML file from a given path and returns its content as a 
    ConfigBox object. It handles exceptions for empty YAML files and logs a success message if the file is loaded correctly.

    Args:
        path_to_yaml (object): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=False):
    """
    This function creates multiple directories at once. It takes a list of directory paths and an optional verbosity flag. 
    If the verbosity flag is True, it logs a message for each created directory. The exist_ok=True argument means that 
    if a directory already exists, it won't raise an error.
    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): ignore if multiple directories is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    This function saves a dictionary (data) to a JSON file at a specified path. 
    It writes the data to the file with indentation for readability and logs a success message with the file path.

    Args:
        path(Path): path to json file
        data(dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    This function loads data from a JSON file at a specified path and returns it as a ConfigBox object, 
    which is a class representation of the data instead of a dictionary. It also logs a success message with the file path.

    Args:
        path(Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    This function saves arbitrary data (data) in binary format to a specified file path (path) using the 
    joblib library and logs a success message.

    Args:
        data(Any): data to be saved in binary format
        path(Path): path to save binary data
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    This function, load_bin, loads binary data from a file at a specified path using joblib.load, 
    logs a success message, and returns the loaded data.

    Args:
        path(Path): path to load binary data

    Returns:
        Any: loaded binary data
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data



@ensure_annotations
def get_size(path: Path) -> str:
    """
    This function calculates the size of a file in kilobytes (KB) and returns it as a string.

    Args:
        path (Path): The path to the file.

    Returns:
        str: The size of the file as a formatted string.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
