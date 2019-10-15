import os
import getpass
import User_Authintication
from Customer import Customer


def clear(): return os.system('cls')


def main():
    clear()
    print("--------------------------------------------------------------------------------")
    print("---------------------- WELCOME TO OUR RJK RETAIL STORE --------------------------")
    print("\n\n")

    answer = input(
        "1- Sign in"
        "\n2- Sign up "
        "\n>>")
    if answer[:1] == '1':
        # User Sign in
        userNameInput = input("Enter your username >> ")
        passwordInput = getpass.getpass("Enter your password >> ")
        adminAssign = 'false'
        User_Authintication.retrieveAllUserInfo(
            userNameInput, passwordInput, adminAssign)

        print("Succesful log in!")
        customerObj = Customer()
        Customer.retrieveCustomerInfo(userNameInput)

    elif answer[:1] == '2':
        newUserInput = input("Enter a unique username! >> ")
        newPassInput = getpass.getpass(
            "Enter a password with a minimum length of 15 characters! >> ")
        User_Authintication.insertUserInfo(newUserInput, newPassInput)
        userNameInput = input("Enter your username >> ")
        passwordInput = getpass.getpass("Enter your password >> ")
        adminAssign = 'false'
        User_Authintication.retrieveAllUserInfo(
            userNameInput, passwordInput, adminAssign)

        print("Succesful log in!")
    else:
        print("Invalid entry\n")


clear()
main()
