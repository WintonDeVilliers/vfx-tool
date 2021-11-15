import json
import os
import re
import sys
from datetime import datetime

import yamldirs.yamldirs_cmd

from dotenv import load_dotenv
from ruamel.yaml import YAML

from FileLoader import *


# load_dotenv("/Users/winstondevilliers/Winton_devWorx/vfx_dir_tool/.env")
# Path variables/ env variables
main_root = os.getenv("MAIN_ROOT")
dir_default_structure = os.getenv("dir_default_structure")
addons = os.getenv("ADDONS")
# continue env vars
mk_construct = os.getenv("mk_construct")
software_construct = os.getenv("software_construct")
"""if publish folder"""
chr_construct = os.getenv("chr_construct")
ep_construct = os.getenv("ep_construct")
_p_global_construct = os.getenv("_p_global_construct")
"""if in folder"""
# temp_construct = no path set
pre_production_construct = os.getenv("pre_production_construct")
# audio_construct = no path set
_2d_construct = os.getenv("_2d_construct")
_3d_construct = os.getenv("_3d_construct")
# references_construct = no path set
shoot_data_construct = os.getenv("SHOOT_DATA")
""" if out folder"""
_approvals_construct = os.getenv("_approvals_construct")
_data_exchange_construct = os.getenv("_data_exchange_construct")
_finals_construct = os.getenv("_finals_construct")
""" if work folder"""
_w_global_construct = os.getenv("_w_global_construct")
_assets_construct = os.getenv("_assets_construct")
tvc_or_flm_construct = os.getenv("tvc_or_flm_construct")
# 101 | shots_construct = path not set


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

    yamldirs.yamldirs_cmd.reconstitute_directory(dir_default_structure)




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
will populate the blocks in blue ie populate the main sub_dirs """


def populate_subdir_master_cfg(user_search_project):
    selected_proj_path = main_root + os.sep + user_search_project + os.sep + "master_cfg"
    # os.chdir(selected_proj_path)
    try:
        for path, sub_dirs, files in os.walk(selected_proj_path):
            for i in sub_dirs:
                if i.endswith("mk"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(mk_construct)
                if i.endswith("software"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(software_construct)
    except FileExistsError as e:
        print(e.__class__, "Subdir already Exists")


def populate_subdir_publish(user_search_project):
    selected_proj_path = main_root + os.sep + user_search_project + os.sep + "publish"
    os.chdir(selected_proj_path)
    try:
        for path, sub_dirs, files in os.walk(selected_proj_path):
            for i in sub_dirs:
                if i.endswith("_chr"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(chr_construct)
                if i.endswith("ep00"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(ep_construct)
                if i.endswith("_global"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(_p_global_construct)

    except FileExistsError as e:
        print(e.__class__, "Subdir already Exists")


def populate_subdir_in(user_search_project):
    selected_proj_path = main_root + os.sep + user_search_project + os.sep + "in"
    os.chdir(selected_proj_path)
    try:
        for path, sub_dirs, files in os.walk(selected_proj_path):
            for i in sub_dirs:
                if i.endswith("pre-production"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(pre_production_construct)
                if i.endswith("2d"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(_2d_construct)
                if i.endswith("3d"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(_3d_construct)
                if i.endswith("shoot_data"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(shoot_data_construct)

    except FileExistsError as e:
        print(e.__class__, "Subdir already Exists")


def populate_subdir_out(user_search_project):
    selected_proj_path = main_root + os.sep + user_search_project + os.sep + "out"
    os.chdir(selected_proj_path)
    try:
        for path, sub_dirs, files in os.walk(selected_proj_path):
            for i in sub_dirs:
                if i.endswith("_approvals"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(_approvals_construct)
                if i.endswith("_data_exchange"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(_data_exchange_construct)
                if i.endswith("_finals"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(_finals_construct)

    except FileExistsError as e:
        print(e.__class__, "Subdir already Exists")


def populate_subdir_work(user_search_project):
    selected_proj_path = main_root + os.sep + user_search_project + os.sep + "work"
    os.chdir(selected_proj_path)
    try:
        for path, sub_dirs, files in os.walk(selected_proj_path):
            for i in sub_dirs:
                if i.endswith("_w_global"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(_w_global_construct)
                if i.endswith("_assets"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(_assets_construct)
                if i.endswith("tvc or flm"):
                    os.chdir(path + os.sep + i)
                    yamldirs.yamldirs_cmd.reconstitute_directory(tvc_or_flm_construct)

    except FileExistsError as e:
        print(e.__class__, "Subdir already Exists")


# ------------------------------------------ Function calls --------------------------------------------------------
# edit_existing_directory("new project", "master_cfg")
# make_default_dirs()
print(os.getcwd())
# directories_2_yaml("/Users/winstondevilliers/RootO/Default1636918899.929845")
# write_json_to_yaml()
# populate_subdir_master_cfg("Default1636918899.929845")
populate_subdir_publish("Default1636918899.929845")
print(os.getcwd())
