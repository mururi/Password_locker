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