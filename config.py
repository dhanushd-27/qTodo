import json
import os
from pathlib import Path

CONFIG_FILE = Path.home() / ".qtodo_config.json"

def get_config():
    if not CONFIG_FILE.exists():
        return {"default_list": "Inbox"}
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {"default_list": "Inbox"}

def save_config(config_data):
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config_data, f, indent=4)
    except OSError as e:
        print(f"Error saving config: {e}")

def get_default_list() -> str:
    return get_config().get("default_list", "Inbox")

def set_default_list(list_name: str):
    config = get_config()
    config["default_list"] = list_name
    save_config(config)
