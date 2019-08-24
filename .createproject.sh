#!/bin/bash

function create() {
    if [[ $# -ge 1 &&  $# -lt 3 ]]
    then
        mkdir "$1"
        python create.py "$1" "$2"
        cd "$1"
        git init
        git remote add origin git@github.com:<Github Username>/$1.git
        touch README.md
        touch .gitignore
        cd ..
    else
        echo -e "Please check the number of arguments are correct.\
        \n *There must be at least 1, project name, description is optional.\
        \n *Please check that your description, if given, is in quotes"
    fi
}