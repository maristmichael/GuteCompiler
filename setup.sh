#!/bin/bash

python3 --version
echo -n "^ Do you see Python3.7 running right now (y/n)? "
read answer

if [ "$answer" != "${answer#[Yy]}" ] ;then
    if [ ! -d "$gutecENV" ]; then
        python3 -m venv ./gutecENV
    fi
    source gutecENV/bin/activate
    which python
    cd src
    pip install --editable .
    cd ..
else
    echo "Please install Python3.7"
    echo "If you have brew, you can run: 'brew upgrade python3' in the terminal,"
    echo "  or download python3.7 directly from the Python website"
fi