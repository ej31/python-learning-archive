import json


def write_json_file(file_path: str = 'state.json', **kwargs):
    """
    Writes JSON file with **kwargs provided.
    :param file_path: Path to write **kwargs data to.
    :param kwargs: Dictionary to dump to JSON file.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(kwargs, f, indent=4)


def load_json_file(json_file: str) -> dict:
    """
    Loads JSON file passed and returns dictionary.
    :param json_file: File to read dictionary from.
    :return: Dictionary with credentials.
    """
    with open(json_file, encoding='utf-8') as f:
        return json.load(f)


if __name__ == '__main__':
    _dict = {
        "key1": True,
        "key2": False,
        "key3": {
            "key3_1": [0, 1, 2, 3, 4, 5]
        }
    }
    write_json_file(**_dict)
    print(load_json_file("state.json"))
