#!/bin/bash

# Define the directory to search for symbolic links
BIN_DIR="/usr/local/bin"

# Function to remove a symbolic link
remove_symlink() {
    echo "Removing symbolic link: $1"
    rm "$1"
}

# Main script execution
echo "Searching for symbolic links to Python in $BIN_DIR..."
find $BIN_DIR -type l -name 'python*' -exec sh -c '
    for symlink; do
        # Check if the symlink points to a Python executable
        if [[ $(readlink "$symlink") == *"/Python.framework/"* ]]; then
            remove_symlink "$symlink"
        fi
    done
' sh {} +

echo "Symbolic links removal process completed."
sudo chmod +x remove_python_symlinks.sh
sudo ./remove_python_symlinks.sh
