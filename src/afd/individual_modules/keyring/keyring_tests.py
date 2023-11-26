import keyring_manager

def test_keyring_manager():
    """
    Test the keyring_manager functions: set, get, delete.
    """

    service = "test_service"
    username = "test_user"
    password = "test_password"

    # Test setting a password
    keyring_manager.manage_credentials("set", service, username, password)
    print("Set Test Passed")

    # Test getting the password
    retrieved_password = keyring_manager.manage_credentials("get", service, username)
    assert retrieved_password == password, "Get Test Failed"
    print("Get Test Passed")

    # Test deleting the password
    keyring_manager.manage_credentials("delete", service, username)
    deleted_password = keyring_manager.manage_credentials("get", service, username)
    assert deleted_password is None, "Delete Test Failed"
    print("Delete Test Passed")

    print("All Tests Passed")

# Run the test
test_keyring_manager()
