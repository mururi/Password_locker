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

def authenticate_user(name, pw):
    """
    Function to authenticate the user
    """

    return User.auth_user(name, pw)


def main():
    print("Welcome to Password Locker App")
    print('\n')
    print("What would you like to do?")
    print('\n')
    
    while True:
        print("Use these short codes: li - log in, su - sign up, ex - exit")
        print("-"*15)
        main_opt = input().lower()
        if main_opt == 'li':
            print("Login to your Password Locker Account")
            print("-"*15)

            print("")