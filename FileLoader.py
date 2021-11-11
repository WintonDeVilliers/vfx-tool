import json
import os
import yaml

from dotenv import load_dotenv


load_dotenv()
main_root = os.getenv("MAIN_ROOT")
top_layer_dir = os.getenv("TOP_LAYER_DIR")
addons = os.getenv("ADDONS")


# will gen the top-level dir structure
def read_yaml_into_program():
    with open(top_layer_dir, 'r+') as new_file:
        dict_version_of_default = yaml.safe_load(new_file)
        real_dict = dict(dict_version_of_default)
        return real_dict


# we currently dumping to yaml file dir_default_structure.yaml in order to use dirs using yamldirs.cmd
def write_json_to_yaml(json_dict):
    with open(top_layer_dir, 'w') as yam_file:
        yaml.dump(json_dict, yam_file)


# we write the changes made by functions/methods to json file dir_yaml_to.json
def write_to_json_file(mutated_json_data):
    with open('dir_yam_to_.json', 'w+') as json_file:
        json.dump(mutated_json_data, json_file)


def read_addons_into_program():
    with open(addons, 'r+') as new_file:
        dict_version_of_default = yaml.safe_load(new_file)
        real_dict = dict(dict_version_of_default)
        return real_dict



def convert_to_xml():
    pass
