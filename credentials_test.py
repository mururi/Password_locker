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

        self.new_credential = Credential("dribbble", "Dennis Kiboi", "dennis.kiboi@student.moringaschool.com", "myDribblePass")

    