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
        test_save_credential test case to test if the credential object is saved into the credentials list
        """

        self.new_credential.save_credential() #saving the new credential
        self.assertEqual(len(Credential.credentials_list), 1)

    def test_save_multiple_credentials(self):
        """
        test_save_credential test case to test if test if multiple credential objects can be saved into the credentials_list
        """

        self.new_credential.save_credential()
        test_credential = Credential("userPlatform", "userName", "user@email.com", "userPass")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list), 2)

    def test_delete_credential(self):
        """
        test_delete_credential test case to test if a credential can be removed from credentials_list
        """

        self.new_credential.save_credential()
        test_credential = Credential("userPlatform", "userName", "user@email.com", "userPass")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credentials_list), 1)

    def test_find_credential_by_platform(self):
        """
        test_find_credential_by_platform test case to test if a credential can be found by the name of the platform
        """

        self.new_credential.save_credential()
        test_credential = Credential("userPlatform", "userName", "user@email.com", "userPass")
        test_credential.save_credential()
        found_credential = Credential.find_by_platform("userPlatform")
        self.assertEqual(found_credential.password, test_credential.password)

    def test_credential_exists(self):
        """
        test_credential_exists test case to test if a credential exists and return a boolean
        """

        self.new_credential.save_credential()
        test_credential = Credential("userPlatform", "userName", "user@email.com", "userPass")
        test_credential.save_credential()
        credential_exists = Credential.credential_exists("userPlatform")
        self.assertTrue(credential_exists)
    

if __name__ == '__main__':
    unittest.main()
    