import requests
import keyring
import logging
from requests.exceptions import RequestException

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ChatGPTAPIConnector:
    def __init__(self):
        # Namespace and username for retrieving API key from keyring
        self.namespace = "ADGE"
        self.username = "GPT_API"

        # Retrieve the API key securely from the keyring
        self.api_key = self.get_api_key()

        # Base URL for the ChatGPT API
        self.base_url = "https://api.openai.com/v1"  # Replace with actual API endpoint

    def get_api_key(self):
        """
        Retrieves the API key from the keyring.
        Raises ValueError if the API key is not found.
        """
        api_key = keyring.get_password(self.namespace, self.username)
        if not api_key:
            logging.error("API key retrieval failed: API key not found in keyring")
            raise ValueError("API key not found in keyring")
        return api_key

    def make_request(self, endpoint, data):
        """
        Makes a POST request to a specified endpoint with given data.
        Args:
            endpoint (str): The API endpoint to make the request to.
            data (dict): The data to be sent in the request.
        Returns:
            dict: The JSON response from the API.
        Raises:
            RequestException: If the request fails.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            # Sending the POST request to the API
            response = requests.post(url, headers=headers, json=data)
            # Raises an HTTPError if the HTTP request returned an unsuccessful status code
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            logging.error(f"Request to {endpoint} failed: {e}")
            raise

    def send_message(self, message):
        """
        Sends a message to the ChatGPT API and returns the response.
        Args:
            message (str): The message to send to the API.
        Returns:
            dict: The response from the API.
        """
        endpoint = "chat"  # Update with the actual endpoint for sending messages
        data = {"message": message}
        return self.make_request(endpoint, data)

    def upload_file(self, file_path):
        """
        Uploads a file to the ChatGPT API.
        Args:
            file_path (str): The path to the file to be uploaded.
        Returns:
            dict: The response from the API.
        Raises:
            RequestException: If the file upload request fails.
        """
        endpoint = "file-upload"  # Replace with the actual file upload endpoint
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "multipart/form-data"
        }

        # Read file content and prepare it for upload
        with open(file_path, 'rb') as file:
            files = {'file': (file_path, file)}
            response = requests.post(self.base_url + '/' + endpoint, headers=headers, files=files)

        try:
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            logging.error(f"File upload failed: {e}")
            raise

# Example usage of the class
if __name__ == "__main__":
    connector = ChatGPTAPIConnector()
    # Example of sending a message
    response = connector.send_message("Hello, world!")
    print(response)
    # Example of uploading a file - Replace 'path/to/your/file.csv' with your file path
    # file_response = connector.upload_file("path/to/your/file.csv")
    # print(file_response)
