import json

def read_json(path):
    """
    Reads a json file and returns the data as a dictionary.
    """
    with open(path, 'r') as f:
        return json.load(f)

def write_json(data, path, indent=2):
    """
    Writes a dictionary to a json file.
    """
    with open(path, 'a') as f:
        json.dump(data, f, indent=indent)