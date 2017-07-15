#!/bin/bash

dd0=$(pwd)
ddd=$(dirname $0)
cd "$ddd"

echo "----- Upgrades -----"
echo "Last check: $(cat time.latest)"
echo "$(cat apt.latest) apt upgrades; $(cat pip2.latest) pip2 upgrades; $(cat pip3.latest) pip3 upgrades"

cd "$dd0"
