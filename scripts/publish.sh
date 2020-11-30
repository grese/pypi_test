#!/bin/bash

###########################################
# Pre-publish (to be run in travis build) #
###########################################

# make sure pip is updated
python3 -m pip install pip
# install latest setuptools, wheel, & twine
python3 -m pip install --user --upgrade setuptools wheel twine

# create dist archive
python3 setup.py sdist bdist_wheel
# publish to pypi
python3 -m twine upload --repository pypi_test dist/*

