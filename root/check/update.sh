#!/bin/bash

cd /root/check; ./apt.sh > apt.latest; ./pip2.sh > pip2.latest; ./pip3.sh > pip3.latest; date > time.latest; ./show.sh
