import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Test class that defines cases for the user class behaviors.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        setUp method to run before each test case. Creates a user object.
        """

        self.new_user = User("Dennis Kiboi", "myPassword")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_user.user_name, "Dennis Kiboi")
        self.assertEqual(self.new_user.user_pass, "myPassword")

    def tearDown(self):
        """
        tearDown method does clean up after each test case has run
        """

        User.users_list = []

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into the user list
        """

        self.new_user.save_user() #save the new user

        self.assertEqual(len(User.users_list), 1)

    def test_save_multiple_users(self):
        """
        test_save_multiple_users to check if we can save multiple user objects to our users_list
        """

        self.new_user.save_user()
        test_user = User("John Doe", "userPass")
        test_user.save_user()

        self.assertEqual(len(User.users_list), 2)

    def test_delete_user(self):
        """
        delete_user method deletes a password locker account
        """

        self.new_user.save_user()
        test_user = User("John Doe", "userPass")
        test_user.save_user()
        
        self.new_user.delete_contact() #delete a user object
        self.assertEqual(len(User.users_list), 1)

        

if __name__ == '__main__':
    unittest.main()