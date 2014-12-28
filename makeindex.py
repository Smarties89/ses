#!/bin/python
# coding: utf-8
import logging
from os import remove, listdir
from os.path import join as join_path
import imp
import json


log = logging.getLogger()


# TODO: Overwrite.
def debug():
    return False

if debug():
    logging.basicConfig()
    log.setLevel(logging.DEBUG)
else:
    logging.basicConfig(filename="ses.txt")


def main(folder, saveto):
    l = []
    for filename in listdir(folder):
        if filename == "index":
            continue
        try:
            obj = imp.load_source("name", join_path(folder, filename))
            l.append(
                {
                    "description": obj.description,
                    "name": filename
                })
            remove(join_path(folder, filename) + "c")
        except:  # We have no idea of knowing what errors can have happend,
                 # since the module is imported and it can leak exceptions.
            log.warning("Failed during makeindex for {}".format(f))


    with open(saveto, "w") as fh:
        json.dump(l, fh)


if __name__ == "__main__":
    main("repo", "repo/index")
