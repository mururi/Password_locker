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

    def tearDown(self):
        """
        tearDown method does clean up after each test case has run
        """

        Credential.credentials_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_credential.platform, "dribbble")
        self.assertEqual(self.new_credential.username, "Dennis Kiboi")
        self.assertEqual(self.new_credential.email, "dennis.kiboi@student.moringaschool.com")
        self.assertEqual(self.new_credential.password, "myDribbblePass")

    def test_save_credential(self):
        """
        test_save_credential test case to test if the user object is saved into the credentials list
        """

        self.new_credential.save_credential() #saving the new credential
        self.assertEqual(len(Credential.credentials_list), 1)

    

    

if __name__ == '__main__':
    unittest.main()
    