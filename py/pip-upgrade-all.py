#!/usr/bin/python

import sys
from subprocess import check_call, check_output, STDOUT, CalledProcessError

PIP_MIN_VERSION = 9

def pip_upgrade_all(pip):
    print("--- Using {} ---".format(pip))
    out = check_output([pip, "--version"])
    version = out.split()[1]
    major = int(version.split(".")[0])
    if major < PIP_MIN_VERSION:
        print("{} version is {}; at least {} is required".format(
            pip, version, PIP_MIN_VERSION))
        return

    out = check_output([pip, "list", "--outdated"])
    packages = []
    for line in out.split("\n")[2:]:
        line = line.strip()
        if not line:
            continue
        name = line.split()[0]
        packages.append(name)
    print("{} packages need to be upgraded".format(len(packages)))
    if not packages:
        return

    print("They are: {}".format(packages))
    try:
        print("Upgrading all packages...")
        check_call([pip, "install", "-U"] + packages, stdout=sys.stdout, stderr=sys.stderr)
    except CalledProcessError:
        print("Upgrade failed. Please upgrade manually, or fix the problem.")
    else:
        print("Upgrade successful.")

if __name__ == "__main__":
    for pip in ['pip2', 'pip3']:
        try:
            pip_upgrade_all(pip)
        except Exception as e:
            print(e)
