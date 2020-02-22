#!/bin/bash

THEME_DIR=flex
THEME_REPO='https://github.com/jdhall75/Flex.git'

if [ -d $THEME_DIR ]; then
    rm -fr $THEME_DIR
fi

git clone $THEME_REPO $THEME_DIR
make clean
pelican -t flex
