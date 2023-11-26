#!/bin/bash

# Define the Python installation directory used by python.org installers
PYTHON_INSTALL_DIR="/Library/Frameworks/Python.framework/Versions/"

# Function to remove a Python installation
remove_python_installation() {
    echo "Removing Python installation at $1"
    # Use 'rm -rf' with caution; here it's used to remove the identified Python directory
    sudo rm -rf "$1"
}

# Main script execution
echo "Searching for Python installations from python.org..."
for dir in "$PYTHON_INSTALL_DIR"/*; do
    # Check if the directory is from python.org by looking for specific files/directories
    if [ -d "$dir" ]; then
        version_dir=$(basename "$dir")
        echo "Found Python version: $version_dir"
        # Here, insert logic to verify if the installation is from python.org
        # If it's a python.org installation, call the remove function
        # Uncomment the following line after adding the verification logic
        # remove_python_installation "$dir"
    fi
done

echo "Python removal process completed."