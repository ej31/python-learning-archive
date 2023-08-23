import json

_dict = {
    "key1": True,
    "key2": False,
    "key3": {
        "key3_1": [0, 1, 2, 3, 4, 5]
    }
}

with open("sample_1.json", "w") as _f:
    json.dump(_dict, _f)

