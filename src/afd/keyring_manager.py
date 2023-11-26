
import keyring
import sys

def manage_credentials(action, namespace, name, secret=None):
    if action == "set":
        keyring.set_secret(namespace, name, secret)
    elif action == "get":
        return keyring.get_secret(namespace, name)
    elif action == "delete":
        keyring.delete_secret(namespace, name)
    else:
        print("Invalid action")

if __name__ == "__main__":
    action = sys.argv[1]
    namespace = sys.argv[2]
    name = sys.argv[3]
    secret = sys.argv[4] if len(sys.argv) > 4 else None

    result = manage_credentials(action, namespace, name, secret)
    if action == "get":
        print(result)
