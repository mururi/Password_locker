import email
import unittest
from credentials import Credential

class TestCredentials(unittest.TestCase):
    """
    Test class that defines cases for the credential class behavior
    Args:
    """

    def setUp(self):
        """
        Set up method to run before each test case.
        """

        self.new_credential = Credential("dribbble", "Dennis Kiboi", "dennis.kiboi@student.moringaschool.com", "myDribbblePass")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_credential.platform, "dribbble")
        self.assertEqual(self.new_credential.username, "Dennis Kiboi")
        self.assertEqual(self.new_credential.email, "dennis.kiboi@student.moringaschool.com")
        self.assertEqual(self.new_credential.password, "myDribbblePass")

if __name__ == '__main__':
    unittest.main()
    