import json


def save_settings(setting_obj):
    with open("settings.json", "w") as file:
        json.dump(setting_obj, file)


def load_settings():
    with open("settings.json", "r") as file:
        return json.load(file)


settings = {"theme": "dark", "language": "en"}
save_settings(settings)

loaded_settings = load_settings()
print(loaded_settings)  # {'theme': 'dark', 'language': 'en'}
