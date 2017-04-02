#!/bin/bash

mkdir ~/bash
cp ./bash/* ~/bash/

mkdir ~/py
cp -r ./py/* ~/py/

cp ./vimrc ~/.vimrc

cp ./ps1 ~/.bash_ps1
echo "Remember to add to the end of ~/.bashrc:"
echo "if [ -f ~/.bash_ps1 ]; then"
echo "    . ~/.bash_ps1"
echo "fi"

