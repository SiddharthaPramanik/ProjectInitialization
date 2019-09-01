#!/bin/bash

function create() {
    if [[ $# -ge 1 &&  $# -lt 3 ]]
    then
        python ~/Documents/Codes/My_Python_Applications/ProjectInitialization/create.py "$1" "$2"
    else
        echo -e "Please check the number of arguments are correct.\
        \n *There must be at least 1, project name, description is optional.\
        \n *Please check that your description, if given, is in quotes"
    fi
}