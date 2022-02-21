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

    def save_user(self):
        """
        save_user method saves an object into users_list
        """

        User.users_list.append(self)

    def delete_user(self):
        """
        delete_user method deletes a saved user from user_list
        """

        User.users_list.remove(self)

    @classmethod
    def auth_user(cls, name, pw):
        """
        auth_user method authenticates user name and password and returns True if they both match an entry in the users list
        """

        for user in cls.users_list:
            if user.user_name == name and user.user_pass == pw:
                return True
        return False