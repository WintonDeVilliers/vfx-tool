import os
import sys

import yaml


def dir_to_dict(path):

    directory = {}

    for dir_name, dir_names, filenames in os.walk(path):
        dn = os.path.basename(dir_name)
        directory[dn] = []

        if dir_name:
            for d in dir_name:
                directory[dn].append(dir_to_dict(path=os.path.join(path, d)))
            for f in filenames:
                directory[dn].append(f)
        else:
            directory[dn] = filenames

        return directory


