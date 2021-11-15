import os
import sys

import yaml


def tree(dirname, **kw):
    exclude = kw.get('exclude', [])
    dirs_only = kw.get('dirs_only', False)

    exclude.append('__pycache__')

    def _tree():
        for rt, dirs, files in os.walk(dirname):
            if not kw.get('dot'):
                for dname in [d for d in dirs if d.startswith('.')]:
                    dirs.remove(dname)
            for d in exclude:
                if d in dirs:
                    dirs.remove(d)
            if dirs_only:
                for d in dirs:
                    yield os.path.join(rt, d)
            else:
                for name in files:
                    if name in exclude:
                        continue
                    if name.endswith('~'):
                        continue
                    if not kw.get('dot'):
                        if name.startswith('.'):
                            continue
                    yield os.path.join(rt, name)

    return list(sorted(_tree()))


def directories_2_yaml(dirname, **args):
    res = {}
    args.pop('dirs_only', None)

    for d in tree(dirname, dirs_only=True, **args):
        parts = d.replace('\\', '/').split('/')
        # print(d, parts)
        cur = res
        for part in parts:
            cur.setdefault(part, {})
            cur = cur[part]
    file = open("/Users/winstondevilliers/Winton_devWorx/vfx_dir_tool/vfx-tool/main.yaml", "w")
    yaml.dump(res, file)
    file.close()

    print(res)

