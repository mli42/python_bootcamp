#!/usr/bin/env zsh

## Usage:
# ./build.sh && pip install ./dist/ai42-1.0.0.tar.gz

### Make sure you have the latest versions of setuptools and wheel installed:
# python3 -m pip install --user --upgrade setuptools wheel

python3 setup.py sdist bdist_wheel
