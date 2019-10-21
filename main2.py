import os
import getpass
import User_Authintication
from Customers import Customer
import re
import psycopg2

# this is my string I used to compare to my birthinput
regex = '[0-9/]$'

# This clears the screen


def clear(): return os.system('cls')

# This is the function for registering the inputs of the new user


def input_valid_name(fieldName):
    while True:
        fieldInput = input("\nEnter your " + fieldName + " >> ")
        if not fieldInput:
            print("Invalid " + fieldName + ", try again")
        else:
            return fieldInput

# The main function of our file


def main():
    clear()
    print("--------------------------------------------------------------------------------")
    print("---------------------- WELCOME TO OUR RJK RETAIL STORE --------------------------")
    print("\n\n")

    print("\n~~~~~~~~~Please select an option below to make your experience at our store much more pleasant!~~~~~~~\n")
    answer = input(
        "1 - Sign in"
        "\n2 - Sign up "
        # "\n3 - Continue as Guest..."
        "\n>> ")
    if answer[:1] == '1':
        # User Sign in
        userHolder = 0
        passholder = 0
        adminAssign = 'false'
        User_Authintication.retrieveAllUserInfo(
            userHolder, passholder, adminAssign)
        customerObj = Customer()
        customerObj.retrieveCustomerInfo(userHolder)

    elif answer[:1] == '2':
        # User Sign up
        customerObj = Customer()
        newUserInput = 0
        newUserInput = customerObj.checkUsername(newUserInput)
        newPassInput = getpass.getpass(
            "\nEnter a password! >> ")
        User_Authintication.insertUserInfo(newUserInput, newPassInput)

        firstNameInput = input_valid_name('first name')
        lastNameInput = input_valid_name('last name')

        while True:
            try:
                phoneInput = int(input_valid_name('phone number'))
                if phoneInput == int(phoneInput):
                    break
            except (Exception, ValueError):
                print("Please enter only numbers!")

        emailInput = input_valid_name('email address')
        addressInput = input_valid_name('home address')

        while True:
            try:
                birthInput = (input_valid_name(
                    'birthday [format:(mm/dd/yyyy)]'))
                if re.search(regex, birthInput):
                    break
                else:
                    print("Please enter only numbers and format as: mm/dd/yyyy !")
            except (Exception, psycopg2.Error):
                print("Please enter correct format!")

        activeAssign = 0
        customerObj.insertCustomerInfo(
            newUserInput, firstNameInput, lastNameInput, phoneInput, emailInput, addressInput, activeAssign, birthInput)

        userNameInput = 0
        passwordInput = 0
        adminAssign = 'false'
        User_Authintication.retrieveAllUserInfo(
            userNameInput, passwordInput, adminAssign)

    else:
        print("Invalid entry\n")


clear()
main()
