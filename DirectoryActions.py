import json
import os
import re
from datetime import datetime

import yamldirs.yamldirs_cmd
# from dotenv import load_dotenv

from FileLoader import *

# main Path env variable
load_dotenv()
main_root = os.getenv("MAIN_ROOT")
top_layer_dir = os.getenv("TOP_LAYER_DIR")
addons = os.getenv("ADDONS")


# will gen the default top-level directory in our main_root folder
def make_default_dirs(default=f"Default{datetime.timestamp(datetime.now())}"):
    project_name_leaf = input(f"Project Name or press ENTER to use {default}")  # this must be a radar selection
    input_check = re.search(r'([a-zA-Z]|[0-9])', project_name_leaf)
    if input_check is None:
        project_name_leaf = default
    os.chdir(main_root)
    os.mkdir(project_name_leaf)
    os.chdir(project_name_leaf)
    yamldirs.yamldirs_cmd.reconstitute_directory(top_layer_dir)


def add_to_given_directory():
    os.chdir(main_root)
    print(os.listdir(main_root))
    user_search_project = input("what project do you want to edit")
    selected_proj_path = main_root + os.sep + user_search_project
    os.chdir(selected_proj_path)
    print(f"Here is a List of options : {os.listdir()}")
    user_subdir_search = input("What subdir do you wish to edit")
    selected_subdir_path = selected_proj_path + os.sep + user_subdir_search
    print(selected_subdir_path)
    # now we show the options that can be added to the subdir
    show_addons = read_addons_into_program()  # .keys()
    print(show_addons.keys())
    for i in addons:
        print(i)
        # for j in addons[i]:
        #     print(j)

    # try for loop for creating subdir
# ------------------------------------------ Function calls --------------------------------------------------------
# read_yaml_into_program()
# user_addon_selection = input("What addon 'type' would you like to add")


# make_default_dirs()  # working well
add_to_given_directory()
# add_to_subdir()
# yamldirs.yamldirs_cmd.reconstitute_directory("dir_default_structure.yaml")
