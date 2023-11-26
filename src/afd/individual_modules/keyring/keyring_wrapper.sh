#!/bin/bash

# Define the path to your Python script
PYTHON_SCRIPT_PATH="keyring_manager.py"

# Check if enough arguments are provided
if [ "$#" -lt 3 ]; then
    echo "Usage: $0 action namespace name [secret]"
    exit 1
fi

# Assigning command line arguments to variables
ACTION=$1
NAMESPACE=$2
NAME=$3
SECRET=$4

# Call the Python script with the provided arguments
if [ "$ACTION" == "set" ] && [ "$#" -eq 4 ]; then
    python $PYTHON_SCRIPT_PATH $ACTION $NAMESPACE $NAME $SECRET
elif [ "$ACTION" == "get" ] || [ "$ACTION" == "delete" ]; then
    python $PYTHON_SCRIPT_PATH $ACTION $NAMESPACE $NAME
else
    echo "Invalid usage or missing arguments."
    echo "For setting a secret, provide: action, namespace, name, and secret."
    echo "For getting or deleting a secret, provide: action, namespace, and name."
    exit 1
fi
