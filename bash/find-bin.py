#!/usr/bin/python

import os

def get_path_list():
    return os.environ["PATH"].split(":")

def match(dirname, filename):
    for name in os.listdir(dirname):
        if filename in name:
            yield os.path.join(dirname, name)

if __name__ == "__main__":
    from sys import argv

    if len(argv) < 2:
        print "Please specify file name"
        exit(1)

    for sys_path_dir in get_path_list():
        for path in match(sys_path_dir, argv[1]):
            print path

