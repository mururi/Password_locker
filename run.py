#!/usr/bin/env python3.8
from platform import platform
import random
import string

from pyrfc3339 import generate
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

def generate_pass(length):
    """
    Function that generates a random password
    """

    password = "".join(random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, length))
    return password

def create_credential(platform, username, email, password):
    """
    Function that creates a new credential
    """

    new_credential = Credential(platform, username, email, password)
    return new_credential

def save_credential(credential):
    """
    Function that saves a new credential to the credentials list
    """

    credential.save_credential()

def display_credentials():
    """
    Function that returns all the saved credentials in the credentials list
    """

    return Credential.display_credentials()

def delete_credential(credential):
    """
    Function that deletes a credential from the credentials list
    """
    credential.delete_credential()



def main():
    print("Welcome to Password Locker App")
    print('\n')
    
    while True:
        print("What would you like to do?")
        print('\n')
        print("Use these short codes: li - log in, su - sign up, ex - exit")
        print("-"*15)
        main_opt = input().lower()
        if main_opt == 'li':
            print("\n")
            print("Login to your Password Locker Account")
            print("-"*15)

            name = input("Enter your username: ")
            pw = input("Enter your password: ")

            if authenticate_user(name, pw):
                print("\n")
                print("LOGIN SUCCESSFUL")
                print("\n")

                while True:
                    print(f"""
                    

                    WELCOME TO YOUR ACCOUNT {name}
                    --------------------
                    Use the following shortcodes:
                    cc - Create new credential
                    dc - Display all your saved credentials
                    fc - Find a saved credential by its platform name
                    dl - Delete a saved credential
                    ex - Log out


                    """)
                    acc_opt = input("What would you like to do?  ").lower()
                    if acc_opt == 'cc':
                        print("\n")
                        print("Create new credential")
                        print("-"*15)
                        platform = input("Enter the Platform: ")
                        username = input("Enter the Username: ")
                        email = input("Enter the Email: ")
                        pass_opt = input("Do you want to generate a password? y/n  ").lower()
                        if pass_opt == 'y':
                            print("\n")
                            length = int(input("Enter the desired password length: "))
                            password = generate_pass(length)
                        else:
                            print("\n")
                            password = input("Enter your password: ")
                        save_credential(create_credential(platform, username, email, password))
                        print("\n")
                        print("New Credentials Successfuly Created")

                    elif acc_opt == 'dc':
                        if 

            else:
                print("LOGIN FAILED: CHECK USERNAME OR EMAIL")

        elif main_opt == 'su':
            print("\n")
            print("Create a Password Locker Account")
            print("-"*15)

            login = input("Enter your preferred Username: ")
            login_pass = input("Enter your preffered Password: ")

            save_user(create_user(login, login_pass))
            print("\n")
            print(f"Your new Username is : {login}")
            print(f"Your new Password is : {login_pass}")

        elif main_opt == 'ex':
            print("GOODBYE!!")
            break

        else:
            print("Wrong entry. Please use the provided short codes.")
