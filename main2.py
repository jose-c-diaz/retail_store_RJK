import os
import getpass
import User_Authintication
from Customer import Customer


def clear(): return os.system('cls')

def input_valid_name(fieldName):
    while True:
        fieldInput = input("Enter your " + fieldName + " >> ")
        if not fieldInput:
            print("Invalid " + fieldName + ", try again")
        else:
            return fieldInput 

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
        customerObj.retrieveCustomerInfo(userNameInput)

    elif answer[:1] == '2':

        newUserInput = input("Enter a unique username! >> ")
        newPassInput = getpass.getpass(
            "Enter a password with a minimum length of 15 characters! >> ")
        User_Authintication.insertUserInfo(newUserInput, newPassInput)

        firstNameInput = input_valid_name("first name") 
        lastNameInput = input_valid_name("last name") 
        phoneInput = input_valid_name("phone number")
        emailInput = input_valid_name("email address")
        addressInput = input_valid_name("home address")
        birthInput = input_valid_name("birthday")

        customerObj = Customer()
        customerObj.insertCustomerInfo(newUserInput, firstNameInput, lastNameInput, phoneInput, emailInput, addressInput, birthInput)

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
