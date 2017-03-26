#!/usr/bin/python

from subprocess import check_output

PIP_MIN_VERSION = 9
pips = ['pip2', 'pip3']

for pip in pips:
    print("Using {}".format(pip))
    out = check_output([pip, "--version"])
    version = out.split()[1]
    major = int(version.split(".")[0])
    if major < PIP_MIN_VERSION:
        print("{} version is {}; at least {} is required".format(
            pip, version, PIP_MIN_VERSION))
        continue
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
        continue
    print("They are: {}".format(packages))
    try:
        out = check_output([pip, "install", "-U"] + packages)
    except:
        print("Upgrade failed. Please upgrade manually, or fix the problem.")
    else:
        print("Upgrade successful.")
