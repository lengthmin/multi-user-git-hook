#!/usr/bin/env python

import os
from configparser import ConfigParser
from pathlib import Path

exit_code = os.system("git config --local user.email >/dev/null")
if (exit_code >> 8) == 0:
    exit(0)

config = ConfigParser()
config.read(Path("~/.gitconfig").expanduser())

section_name = "multi"

sections = config.sections()

pwd = str(Path(".").absolute())
print("pwd: ", pwd)
for section in sections:
    if section.startswith(section_name):
        dct = dict(config[section].items())
        to_set = {}
        part = dct.pop("has", "")
        flag = part in pwd

        for key, value in dct.items():
            command = ".".join(key.split("-"))
            to_set[command] = value
        if flag:
            for k, v in to_set.items():
                cmd = f"git config --local {k} {v}"
                os.system(cmd)
                print(cmd)
            print(
                "Setting local info\n",
                "Commit again if these are correct.",
            )
            exit(1)
