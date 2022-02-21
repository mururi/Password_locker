#!/usr/bin/env python3.8
from user import User
from credentials import Credential

def create_user(login, login_pass):
    """
    Function to create a new user
    """

    new_user = User(login, login_pass)
    return new_user

def save_user(user):
    """
    Function that saves user details to users_list
    """

    user.save_user()

