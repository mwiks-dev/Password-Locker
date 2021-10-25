import random
from user import User
from credentials import Credentials

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(uname):
    '''
    Function that finds a user by name and returns the user
    '''
    return uname.find_by_name(uname)

def create_credentials(accountname,loginkey):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(accountname,loginkey)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete credentials
    '''
    credentials.delete_credentials()

def find_credentials(aname):
    '''
    Function that finds credentials by accountname and returns the credential
    '''
    return aname.find_by_name(aname)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print('Hello! Welcome to Password Locker.')
    print('\n')

    print('What would you like to do? Find ways to navigate around below.')
    print('\n')

    while True:
        print("Use these short codes 'lg': to Login to your account, 'sg' to sign-up and create an account,'du' to delete a user account,'dc' to display credentials, 'ex' to exit the application.")
        short_code = input().lower()
        print('\n')
        if short_code == 'sg':
                            print("Enter username")
                            username = input()

                            print ("Enter password")
                            password = input()
                            
                            print ("Confirm password")
                            confirm_password = input()

                            while confirm_password != password:
                                print("Passwords did not match! Kindly try again")
                                print("Enter password")
                                password = input()
                                print("Confirm password")
                                confirm_password = input()
                            else :
                                print(f"Congratulations {username}! Your account was created successfully!")
                                print('\n')
                                print("Please proceed to login")
                                print("Enter username")
                                entered_username = input()
                                print("Enter password")
                                entered_password = input()
                            
                            while entered_username != username or entered_password != password:
                                print("Invalid username or password")

                                print("Enter your username")
                                entered_username = input()
                                print("Enter your password")
                                entered_password = input()

                            else:
                                print(f"Welcome to your account {username}")
                                
        
        elif short_code == 'lg':
            print("Enter username")
            default_username = input()
            print("Enter password")
            default_password = input()

            while default_username != 'Vodca' or default_password != 'Angela22':
                print("Wrong username or password")
                
            else:
                print("Login success!:)")

        elif short_code == 'dc':
            if display_credentials():
                print("Find a list of your credentials below")
                print('\n')
                
                for credentials in display_credentials():
                    print(f"{credentials.accountname} {credentials.password}")
                    print("\n")

            else:
                print ("You dont have any saved credentials yet!")


        elif short_code == 'ex':
            break

        else:
            print("Enter valid to continue!")

if __name__ == "__main__":
    main()