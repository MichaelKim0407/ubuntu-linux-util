#!/usr/bin/python

import os

DRIVE_LIST = "/dev"
LOCAL_FILE_NAME = os.path.join(os.path.dirname(__file__), "internal-drives.local")

def list_drives():
    return os.listdir(DRIVE_LIST)

def list_internal():
    with open(LOCAL_FILE_NAME) as f:
        for line in f:
            if line.endswith("\n"):
                line = line[:-1]
            yield line

if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1 and argv[1] == "--update":
        try:
            l = list_drives()
            with open(LOCAL_FILE_NAME, "w") as f:
                for item in l:
                    f.write("{}\n".format(item))
        except Exception:
            print "Updating failed with code {}".format(stat)
            print "You can manually update internal drives by 'ls /dev > internal-drives.local'"
    else:
        l_internal = list(list_internal())
        matches = argv[1:]
        for item in list_drives():
            if item in l_internal:
                continue
            if not matches:
                print item
            else:
                for m in matches:
                    if m in item:
                        print item
                        break


