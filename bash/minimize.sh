#!/bin/bash
opt="true"
if [ $1 ]
then
    opt="$1"
fi
gsettings set org.compiz.unityshell:/org/compiz/profiles/unity/plugins/unityshell/ launcher-minimize-window $opt

