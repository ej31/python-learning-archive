import json

with open("sample_1.json", "r") as f:
    _dict_by_file = json.load(f)
    print(_dict_by_file)

