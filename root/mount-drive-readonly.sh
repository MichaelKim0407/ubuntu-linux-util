#!/bin/bash

if [[ -z "$1" ]]
then
    echo "Please specify drive id"
    echo "You can get a list of drive ids by 'ls /dev'"
    exit 1
fi

dev=/dev/$1
media=/media/${USER}/$1
exist=$(ls /media/${USER} | grep $1)

if [[ -z "${exist}" ]]
then
    echo "Mounting ${dev} as ${media} (readonly)"
    mkdir ${media} && mount -o ro ${dev} ${media}
else
    echo "Unmounting ${dev} | ${media}"
    umount ${media}
    rm -r ${media}
fi
