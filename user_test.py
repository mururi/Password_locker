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
        self.assertEqual(self.new_user.user_name, "Dennis Kiboi")
        self.assertEqual(self.new_user.user_pass, "myPassword")

if __name__ == '__main__':
    unittest.main()