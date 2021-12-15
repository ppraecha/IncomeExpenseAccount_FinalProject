import json


def save_data(target_dict, target_file):
    with open(target_file, "w") as f:
        json.dump(target_dict, f)
        f.close()


def load_data(target_file):
    with open(target_file, "r") as fr:
        return json.load(fr)
