from typing import List, Dict, Any
import json

def read_json(file_path: str) -> Dict[str, Any]:
    """Read a JSON file and return its content as a dictionary.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        Dict[str, Any]: The content of the JSON file as a dictionary.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path: str, data: Dict[str, Any]) -> None:
    """Write a dictionary to a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        data (Dict[str, Any]): The data to write to the file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def find_value_in_dict(data: Dict[str, Any], key: str) -> List[Any]:
    """Find all values for a given key in a nested dictionary.

    Args:
        data (Dict[str, Any]): The nested dictionary to search.
        key (str): The key to find.

    Returns:
        List[Any]: A list of values associated with the key.
    """
    values = []
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                values.append(v)
            values.extend(find_value_in_dict(v, key))
    elif isinstance(data, list):
        for item in data:
            values.extend(find_value_in_dict(item, key))
    return values
