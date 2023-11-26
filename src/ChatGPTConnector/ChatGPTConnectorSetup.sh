#!/bin/bash

# Function to check if Python 3.11.4 is installed
check_python_version() {
    version=$(python3.11 --version 2>&1)
    if [[ $version == *"Python 3.11.4"* ]]; then
        echo "Python 3.11.4 is installed"
    else
        echo "Python 3.11.4 is not installed. Please install Python 3.11.4"
        exit 1
    fi
}

# Function to create and activate virtual environment
create_and_activate_venv() {
    python3.11 -m venv venv
    source venv/bin/activate
}

# Function to set up the API key in keyring
setup_api_key() {
    echo "Please enter your ChatGPT API key:"
    read -s api_key
    python3.11 -c "import keyring; keyring.set_password('ADGE', 'GPT_API', '$api_key')"
    echo "API key has been stored securely in keyring."
}

# Function to install required Python libraries
install_libraries() {
    pip install requests
    pip install keyring
    pip install logging
}

# Check Python version
check_python_version

# Create and activate virtual environment
create_and_activate_venv

# Install required libraries
install_libraries

# Enter your API Key
setup_api_key

echo "Setup completed successfully."
