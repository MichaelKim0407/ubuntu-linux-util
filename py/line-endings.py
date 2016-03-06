#!/usr/bin/python

import os
import logging

FROM = "\r\n"
TO = "\n"
INCLUDE = []
EXCLUDE = []

logger = logging.getLogger("line-endings")

def has_any(name, l):
    for item in l:
        if item in name:
            return True
    return False

def recursive(func):
    def new_func(folder, *args, **kwargs):
        for fname in os.listdir(folder):
            path = os.path.join(folder, fname)
            if has_any(path, EXCLUDE):
                continue
            if os.path.isfile(path):
                if INCLUDE and not has_any(path, INCLUDE):
                    continue
                count = func(path, *args, **kwargs)
                logger.info("In {:<64}: {:>8} lines converted".format(path, count))
            else:
                new_func(path, *args, **kwargs)
    return new_func

@recursive
def convert(filename):
    with open(filename) as f:
        text = f.read()
    count = text.count(FROM)
    if count > 0:
        text = text.replace(FROM, TO)
        with open(filename, "w") as f:
            f.write(text)
    return count

def print_help():
    print """line-endings.py [options] [includes] [! excludes]

Options:
    -h  --help      Show help
    -r  --revert    Convert "\\n" to "\\r\\n"

Includes:
    All files whose relative path contains any of these will be included.
    If omitted, all files are included.

Excludes:
    All files whose relative path contains any of these will be excluded.
"""

if __name__ == "__main__":
    from sys import argv
    args = argv[1:]

    logging.basicConfig(
            level=logging.INFO,
            format="[%(levelname)s] %(message)s"
            )

    # Options
    while args and args[0].startswith("-"):
        if args[0] in ["-h", "--help"]:
            print_help()
            exit(0)
        elif args[0] in ["-r", "--revert"]:
            FROM, TO = TO, FROM
            logger.info("Option specified: Revert from \\n to \\r\\n")
        args = args[1:]

    # Includes
    while args and args[0] != "!":
        INCLUDE.append(args[0])
        args = args[1:]
    logger.info("Includes: {}".format(INCLUDE))

    # Excludes
    if args and args[0] == "!":
        args = args[1:]
    while args:
        EXCLUDE.append(args[0])
        args = args[1:]
    logger.info("Excludes: {}".format(EXCLUDE))

    convert(".")

