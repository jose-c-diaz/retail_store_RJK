#from Employee import Employee

from Categories import Categories
from Products import Products
import ShoppingCart
import psycopg2
import re
import os
import getpass
import hashlib
import binascii

from colorama import Fore, Back, Style


def clear(): return os.system('cls')


def colorGreen():
    print("\033[1;37;32m")


def colorWhite():
    print("\033[1;37;40m")


def colorBlue():
    print("\n\n\033[1;34;40m")


def logo():
    colorGreen()
    #print("                                                                                  ")
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
    print("  _______        _____   ___  ____     _______            _          _     __   ")
    print(
        " |_  __  \      |_   _| |_  ||_  _|   |_  __  \          / |_       (_)   [  |  ")
    print("  | |__) |        | |    | |_/ /       | |__) |   .---. `| |-',--.   __    | |  ")
    print(
        "  |  __ /     _   | |    |  __'.       |  __ /   / /__\\  | | `'_\ : [  |   | |  ")
    print(" _| |  \ \_  | |__' |   _| |  \ \_    _| |  \ \_ \ \__., | |,// | |, | |   | |  ")
    print(
        " |____| |___| `.____.'  |____||____|  |____| |___| '.__.' \__/\'-;__|[___| |___] ")
    print(" \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    # print("                                                                                  ")

    colorWhite()
    print("--------------------------------------------------------------------------------")
    print("---------------------- WELCOME TO OUR ONLINE RETAIL STORE ----------------------")


def adminMenu():
    print("                   ~~ Administration MAIN MENUE ~~\n\n")
    print("                       1- Manage Categories")
    print("                       2- Manage Products")
    print("                       3- Manage Customers\n")
    manageGRP = input("Please choose your option [1-3] >>")
    # admin select manage categories
    if manageGRP[:1] == '1':
        clear()
        Category = Categories()
        Category.main()
        # admin select manage Products
    elif manageGRP[:1] == '2':
        clear()
        product = Products()
        product.main()
        # admin select manage Customers
    elif manageGRP[:1] == '3':
        clear()
        # Category = Categories()
        # Category.main()
    else:
        print("Invalid Option")


def placeOrder(product, ProductCounter, rows):

    productNo = input(
        "\n\nPlease enter a valid product from the list above >> ")
    if product.ValidateUserInputAsNumber(productNo):
        productNo = int(productNo)
        if(productNo > 0 and productNo <= ProductCounter and productNo is not None):
            rowIndex = int(productNo)-1
            amount = input("Please enter the amount value>> ")
            if(product.ValidateUserInputAsNumber(amount)):
                if(int(amount) > 0):

                    ShoppingCart.addProductToShppingCart(
                        rows[rowIndex], amount)


def customerMenue():
    print("Welcome Rinad to RJK store")
    print("We have these products available for your order:")
    print("\n                   ~~ PRODUCTS LIST ~~\n\n")
    product = Products()
    cursor = product.retriveProductsOrderByCategory()
    rows = cursor.fetchall()
    if(rows):

        categoryCount = 0
        categoryNo = 0
        ProductCounter = 0
        for row in rows:

            if (categoryNo != int(row[0])):
                categoryNo = int(row[0])
                print(f"\n- {row[1]} :-")
                categoryCount += 1
            print(f"                {ProductCounter+1} - {row[3]}")
            print(f"                Price= {row[5]}")
            print(f"                {row[4]}")
            ProductCounter += 1

    print("1- Place Order")
    print("2- Search spesific product")
    customerOption = input("What do you want to do? ")

    if product.ValidateUserInputAsNumber(customerOption):
        customerOption = int(customerOption)
        if(customerOption > 0 and customerOption <= 2 and customerOption is not None):
            if(customerOption == 1):
                print("You decided to place order!")

                placeOrder(product, ProductCounter, rows)
                orderFlag = True
                while(orderFlag):
                    confirmOrder = input(
                        "Do you want to order something else? Y|N>>")
                    if(str.upper(confirmOrder) == "YES" or str.upper(confirmOrder) == "NO" or str.upper(confirmOrder) == "Y" or str.upper(confirmOrder) == "N"):
                        if(str.upper(confirmOrder) == "YES" or str.upper(confirmOrder) == "Y"):
                            whileLoopFlag = True
                            orderFlag = True
                            placeOrder(product, ProductCounter, rows)

                        else:
                            whileLoopFlag = False
                            orderFlag = False
                    else:
                        print("Invalid Option")
                        whileLoopFlag = True
                        orderFlag = True

                clear()
                ShoppingCart.printShoppingCart()
            else:
                print("Search Product by name")
                print("\n\n- Search Products by Name -")
                productName = input(
                    "Please enter a keyword to search for Product Name >> ")
                whereStatment = f"LOWER(product_name) like '%{productName}%' "


def main():
    clear()
    logo()
    colorBlue()
    print(
        "Welcome & Thank You For Visiting Our Online Store.")
    print("We're Happy to Provide You With Good Quality Products At a Low Cost... ")
    print("Don't Forget About Our Free Shipping For Orders Over 50$ !")
    colorWhite()
    print("\n\n\n---------------------")

    answer = input(
        "1- Sign in"
        "\n2- Sign up "
        "\n>>")

    if answer[:1] == '1':

        clear()
        print("Succesful log in!")
        clear()
        logo()
        print("\n\n")

        IsuserAdmin = True
        if(IsuserAdmin):
            adminMenu()
        #User is customer
        else:
            customerMenue()


clear()

main()
