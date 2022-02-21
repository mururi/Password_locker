class Credential:
    """
    Class that generates new instance of credentials
    """

    credentials_list = []

    def __init__(self, platform, username, email, password):
        """
        __init__ method creates an instance of Credential class
        """

        self.platform = platform
        self.username = username
        self.email = email
        self.password = password

    def save_credential(self):
        """
        save_credential method saves credential object into credentials_list
        """

        Credential.credentials_list.append(self)

    def delete_credential(self):
        """
        delete_credential method deletes a saved contact from the credentials_list
        """

        Credential.credentials_list.remove(self)