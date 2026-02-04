import json


def save_json(data):
    with open(file="outpout.json", mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True, ensure_ascii=False)
