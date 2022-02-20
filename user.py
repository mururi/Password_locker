class User:
    """
    Class that generates new instances of users
    """

    users_list = []

    def __init__(self, user_name, user_pass):
        """
        __init__ method creates an instance of user class
        """

        self.user_name = user_name
        self.user_pass = user_pass