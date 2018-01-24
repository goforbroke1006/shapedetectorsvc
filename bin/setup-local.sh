#!/usr/bin/env bash

if [ -f /etc/lsb-release ]; then # Ubuntu
    sudo apt-get install -y python-opencv
    pip install --upgrade pip
    sudo pip install -r ./requirements.txt
else
    echo Your OS is not supported: $(uname -s) $(uname -r)
fi