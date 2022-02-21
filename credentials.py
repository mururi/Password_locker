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

    @classmethod
    def find_by_platform(cls, platform):
        """
        find_by_platform method takes in a platform name and returns a credential that matches that platform name

        Args:
            platform: platform name to search for
        Returns:
            Credential that matches the platform name
        """

        for credential in cls.credentials_list:
            if credential.platform == platform:
                return credential

    @classmethod
    def credential_exists(cls, platform):
        """
        credential_exists method checks if a credential exists in the credentials list
        
        Args:
            platform: platform name to search for
        Returns:
            Boolean: True or false depending on if the credential exists
        """

        for credential in cls.credentials_list:
            if credential.platform == platform:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        display_credentials method returns the credentials list
        """

        return cls.credentials_list
        