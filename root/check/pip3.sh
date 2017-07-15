#!/bin/bash

aaa=$(/usr/local/bin/pip3 list --outdated)

if [ -z "$aaa" ]
then
    echo 0
    exit 0
fi

nnn=$(echo "$aaa" | wc -l)
nnn=$(expr "$nnn" - 2)
echo $nnn
