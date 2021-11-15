import json
import os
import yaml
import yamldirs
import yamldirs.yamldirs_cmd
from dotenv import load_dotenv


load_dotenv()
main_root = os.getenv("MAIN_ROOT")
dir_default_structure = os.getenv("dir_default_structure")
addons = os.getenv("ADDONS")


# will gen the top-level dir structure
def read_yaml_into_program():
    with open(dir_default_structure, 'r+') as new_file:
        dict_version_of_default = yaml.safe_load(new_file)
        real_dict = dict(dict_version_of_default)
        return real_dict


# we currently dumping to yaml file dir_default_structure.yaml in order to use dirs using yamldirs.cmd
def write_json_to_yaml():
    with open("/Users/winstondevilliers/Winton_devWorx/vfx_dir_tool/vfx-tool/main.yaml", 'w') as yam_file:
        data = yamldirs.yamldirs_cmd.directories2yaml("/Users/winstondevilliers/RootO/Default1636918899.929845")
        print(data)
        yaml.dump(data, yam_file)


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
