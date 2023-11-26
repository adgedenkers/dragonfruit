# ChatGPT API Connector

This project provides a Python class for interacting with the ChatGPT API. It includes capabilities for sending messages, handling file uploads, and securely managing API keys.

## Setup

### Prerequisites

- Python 3.11.4

### Environment Setup

1. **Clone the Repository**
   - Clone this repository to your local machine.

2. **Run the Setup Script**
   - Execute the `setup.sh` script to create a virtual environment and install the required dependencies.
   - The script will prompt you to enter your ChatGPT API key, which will be stored securely in the keyring.

   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
3. **Activate the Virtual Environment**
   - Whenever you start a new terminal session, activate the virtual environment:
   ```
   source venv/bin/activate
   ```
   
# Usage

## ChatGPTApiConnector Class

The ChatGPTAPIConnector class provides methods to interact with the ChatGPT API.

- **Sending Messages**
  - Use the send_message method to send a text message to the ChatGPT API and receive a response.

```python
connector = ChatGPTAPIConnector()
response = connector.send_message("Hello, world!")
print(response)
```

- **Uploading Files**
  - The upload_file method allows you to upload files, such as CSV or text files, to the ChatGPT API.

```python
file_response = connector.upload_file("path/to/your/file.csv")
print(file_response)
```

## Use Cases
1. **Text Interaction**
   - Interact with ChatGPT to get responses to queries, have a conversation, or receive text-based assistance.
2. **Data Analysis**
   - Upload data files (e.g., CSV) for analysis or processing by ChatGPT. Useful for summarizing or interpreting data.
3. **Educational Tool**
   - Use ChatGPT to answer educational queries or assist in learning new topics.
4. **Automation Scripts**
   - Integrate the connector into larger Python scripts to automate interactions with ChatGPT for various purposes.

## Security

The API key is stored securely using the keyring library. Ensure not to expose your API key in scripts or logs.
 