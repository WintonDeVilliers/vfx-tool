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
"""LAYER 1"""


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
    # os.chdir(main_root)
    #
    # print(f"Projects to select from : {os.listdir(main_root)}")
    #
    # user_search_project = input("What project do you want to edit: ")
    #
    # selected_proj_path = main_root + os.sep + user_search_project
    #
    # os.chdir(selected_proj_path)
    #
    # print(f"List of Directory/Folder options : {os.listdir()}")
    #
    # user_subdir_search = input("What subdir do you wish to edit: ")
    #
    # selected_subdir_path = selected_proj_path + os.sep + user_subdir_search
    #
    # os.chdir(selected_subdir_path)

    show_addons = read_addons_into_program()

    print(show_addons)

    user_addon_selection = input(f"What addon would you like to add to Folder:   ")

    # now we show the options that can be added to the subdir
    # print(user_addon_selection)
    for key, value in show_addons.items():
        if user_addon_selection != value:
            print(user_addon_selection)
            print(value[user_addon_selection])



def edit_existing_directory():
    os.chdir(main_root)
    user_search_project = input("What project do you want to edit: ")
    selected_proj_path = main_root + os.sep + user_search_project
    os.chdir(selected_proj_path)
    # at this point we are in the dir and have sight of the base folders
    for path, sub_dirs, files in os.walk(selected_proj_path):
        # if path in sub_dirs:
        for i in sub_dirs:
            print(path)
            # main_root + os.sep + user_search_project + os.sep + folder_to_edit



# ------------------------------------------ Function calls --------------------------------------------------------
# make_default_dirs()
# edit_existing_directory()
# add_to_given_directory()
# add_to_subdir()
# yamldirs.yamldirs_cmd.reconstitute_directory("dir_default_structure.yaml")
