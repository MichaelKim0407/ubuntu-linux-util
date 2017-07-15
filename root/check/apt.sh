#!/bin/bash

aaa=$(apt update)

yyy=$(echo "$aaa" | grep "All packages are up to date.")
if [ -n "$yyy" ]
then
    echo 0
    exit 0
fi

echo "$aaa" | grep -oP "([0-9]*)(?= packages? can be upgraded.)"
