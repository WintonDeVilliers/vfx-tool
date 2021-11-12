import json
import os
import re
from datetime import datetime

import yamldirs.yamldirs_cmd
# from dotenv import load_dotenv

from FileLoader import *

# Path variables/ env variables
load_dotenv()
main_root = os.getenv("MAIN_ROOT")
top_layer_dir = os.getenv("TOP_LAYER_DIR")
addons = os.getenv("ADDONS")
# continue env vars
mk_construct = os.getenv("MK")
software_construct = os.getenv("SOFTWARE")
"""if in folder"""
# temp_construct = no path set
pre_production_construct = os.getenv("PRE_PRODUCTION")
# audio_construct = no path set
_2d_construct = os.getenv("_2D")
_3d_construct = os.getenv("_3D")
# references_construct = no path set
shoot_data_construct = os.getenv("SHOOT_DATA")
""" if out folder"""
_approvals_construct = os.getenv("_APPROVALS")
_data_exchange_construct = os.getenv("_DATA_EXCHANGE")
_finals_construct = os.getenv("_FINALS")
""" if work folder"""
_global_construct = os.getenv("_GLOBAL")
assets_construct = os.getenv("ASSETS")
TVC_or_FLM_construct = os.getenv("TVC_OR_FLM")
# shots_construct = path not set



"""LAYER 1 & 2
will activate first two blocks """


# will gen the default top-level directory in our main_root folder
def make_default_dirs(default=f"Default{datetime.timestamp(datetime.now())}"):
    project_name_leaf = input(f"Project Name or press ENTER to use {default} :")  # this must be a radar selection
    input_check = re.search(r'([a-zA-Z]|[0-9])', project_name_leaf)

    if input_check is None:

        project_name_leaf = default

    os.chdir(main_root)

    os.mkdir(project_name_leaf)

    os.chdir(project_name_leaf)

    yamldirs.yamldirs_cmd.reconstitute_directory(top_layer_dir)


"""def add_to_given_directory():
    os.chdir(main_root)

    print(f"Projects to select from : {os.listdir(main_root)}")

    user_search_project = input("What project do you want to edit: ")

    selected_proj_path = main_root + os.sep + user_search_project

    os.chdir(selected_proj_path)

    print(f"List of Directory/Folder options : {os.listdir()}")

    user_subdir_search = input("What subdir do you wish to edit: ")

    selected_subdir_path = selected_proj_path + os.sep + user_subdir_search

    os.chdir(selected_subdir_path)

    show_addons = read_addons_into_program()

    print(show_addons)

    user_addon_selection = input(f"What addon would you like to add to Folder:   ")

    # now we show the options that can be added to the subdir
    # print(user_addon_selection)
    for key, value in show_addons.items():
        if user_addon_selection != value:
            print(user_addon_selection)
            print(value[user_addon_selection])"""


"""Layer 3
will activate blocks of dirs we will try positional args, 
with the view changing it at next refactor to accommodate **kwargs"""


def edit_existing_directory(user_search_project, master_cfg=None, in_folder=None, out_folder=None, work=None):
    os.chdir(main_root)
    # user_search_project = input("What project do you want to edit: ")
    selected_proj_path = main_root + os.sep + user_search_project
    os.chdir(selected_proj_path)
    # at this point we are in the dir and have sight of the base folders
    # here want to create an activation switch for the Layer 2 Directories...activating them block by block or all at once
    if master_cfg is not None:
        for path, sub_dirs, files in os.walk(selected_proj_path):
            for i in sub_dirs:
                if i.endswith("mk"):
                    os.chdir(path + os.sep + "mk")
                    yamldirs.yamldirs_cmd.reconstitute_directory(mk_construct)
                if i.endswith("software"):
                    os.chdir(path + os.sep + "software")
                    yamldirs.yamldirs_cmd.reconstitute_directory(software_construct)
    #     # we want to cd to dir and mkdir
    #     for path, sub_dirs, files in os.walk(selected_proj_path):
    #     pass
    # elif args == "in":
    #     pass
    # elif args == "out":
    #     pass
    # elif args == "work":
    #     pass
    # else:
    #     pass
    # for path, sub_dirs, files in os.walk(selected_proj_path):
    #     # if path in sub_dirs:
    #     for i in sub_dirs:
    #         if i.endswith("mk"):
    #             os.chdir(path + os.sep + "mk")
    #             print(os.getcwd())
    #             yamldirs.yamldirs_cmd.reconstitute_directory(mk_construct)


# edit_existing_directory("new project", "master_cfg")
make_default_dirs()
# ------------------------------------------ Function calls --------------------------------------------------------
# make_default_dirs()

# add_to_given_directory()
# add_to_subdir()
# yamldirs.yamldirs_cmd.reconstitute_directory("dir_default_structure.yaml")
