#!/usr/bin/env python3.8
from platform import platform
from rich import print
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

def check_existing_credential(platform):
    """
    Fuction that checks the credentials list to see if a credential exists and returns a boolean
    """

    return Credential.credential_exists(platform)

def find_credential(platform):
    """
    Function that finds an existing credential and returns the dictionary
    """

    return Credential.find_by_platform(platform)

def delete_credential(credential):
    """
    Function that deletes a credential from the credentials list
    """
    credential.delete_credential()



def main():
    print("""
    
    [blue bold]Welcome to Password Locker App[/blue bold]
    """)
    print('\n')
    
    while True:
        print("\n")
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
                print("[green]LOGIN SUCCESSFUL[/green]")
                print("\n")

                while True:
                    print(f"""
                    

                    WELCOME TO YOUR ACCOUNT {name}
                    --------------------
                    Use the following shortcodes:
                    cc - Create new credential
                    dc - Display all your saved credentials
                    fc - Find a saved credential by its platform name
                    xc - Delete a saved credential
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
                        print("\n")

                    elif acc_opt == 'dc':
                        if display_credentials():
                            print("\n")
                            print("Here is a list of all your credentials")
                            print("-"*15)
                            for credential in display_credentials():
                                print(f"""
                                {credential.platform}
                                {credential.username}
                                {credential.email}
                                {credential.password}
                                """)
                                print("\n")
                        else:
                            print("\n")
                            print("You don't seem to have any credentials saved yet")
                            print("\n")
                    
                    elif acc_opt == 'fc':
                        print("\n")
                        search_platform = input("Enter the name of the platform whose credentials you want to find: ")
                        if check_existing_credential(search_platform):
                            search_credential = find_credential(search_platform)
                            print("\n")
                            print(f"""
                            
                            {search_credential.platform}
                            {search_credential.username}
                            {search_credential.email}
                            {search_credential.password}

                            """)
                        else:
                            print("\n")
                            print("That credential does not exist")
                            print("\n")

                    elif acc_opt == 'xc':
                        print("\n")
                        del_platform = input("Enter the name of the platform whose credentials you want to delete: ")
                        if check_existing_credential(del_platform):
                            delete_credential(find_credential(del_platform))
                            print(f"Credentials for {del_platform} have been successfully deleted.")
                        else:
                            print("\n")
                            print("That credential does not exist")
                            print("\n")

                    elif acc_opt == 'ex':
                        print("\n")
                        print("YOU ARE LOGGED OUT. BYE!")
                        print("\n")
                        break

                    else:
                        print("\n")
                        print("Please enter a valid keyword")
                        print("\n")

            else:
                print("[red]LOGIN FAILED: CHECK USERNAME OR EMAIL[/red]")

        elif main_opt == 'su':
            print("\n")
            print("Create a Password Locker Account")
            print("-"*15)

            login = input("Enter your preferred Username: ")
            login_pass = input("Enter your preffered Password: ")

            save_user(create_user(login, login_pass))
            print("\n")
            print(f"""Your new Username is : {login}
                    Your new Password is : {login_pass}
                """)

        elif main_opt == 'ex':
            print("GOODBYE!!")
            break

        else:
            print("Wrong entry. Please use the provided short codes.")

if __name__ == "__main__":
    main()
