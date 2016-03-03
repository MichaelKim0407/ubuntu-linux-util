#!/bin/bash

if [ -z "$1" ]
then
    echo "Please specify drive id"
    echo "You can get a list of drive ids by 'ls /dev'"
    exit 1
fi

dev=/dev/$1
media=/media/$USER/$1
exist=$(ls /media/$USER | grep $1)
if [ -z "$exist" ]
then
    echo "Mounting $dev as $media (readonly)"
    sudo mkdir $media && sudo mount -o ro $dev $media
else
    echo "Unmounting $dev | $media"
    sudo umount $media
    sudo rm -r $media
fi

