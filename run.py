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
                    acc_opt = input("What would you like to do?  ")
                    if acc_opt == 'cc':
                        print("\n")
                        print("Create new credential")
                        print("-"*15)
                        

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

if __name__ == '__main__':
    main()