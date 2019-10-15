
from Employee import Employee
from Category import Category
import psycopg2
import os
import getpass
import hashlib
import binascii


def clear(): return os.system('cls')

# This function is to build dynamic select statment


def selectStatment(tableName, WhereStatment):
    selectStatment = "SELECT * FROM " + tableName + " WHERE " + WhereStatment
    return selectStatment

# This function to Execute the sql command and return the data set


def retreiveDataFromDBTables(selectStatment):
    try:
        conn = psycopg2.connect(
            database="RetailStore",
            user="postgres",
            password="6108",
            host="127.0.0.1",
            port="5432"
        )
    except(Exception, psycopg2.Error)as err:
        print("Error while fetching data from PostgreSQL", err)

    cursor = conn.cursor()
    cursor.execute(selectStatment)
    rows = cursor.fetchall()
    cursor.close()
    return rows


def selectSpesificRealState(realStateID, sellOrBuy):
    try:
        conn = psycopg2.connect(
            database="Real_Investments",
            user="postgres",
            password="6108",
            host="127.0.0.1",
            port="5432"
        )
    except(Exception, psycopg2.Error)as err:
        print("Error while fetching data from PostgreSQL", err)

        # Retrive real state data from database
    cursor = conn.cursor()
    cursor.execute(
        f"select * from real_state where real_state_id='{realStateID}'")
    rows = cursor.fetchall()
    if(rows):

        for row in rows:

            house.real_state_id = row[0]
            house.real_state_name = row[1]
            house.real_state_address = row[3]
            house.no_of_bedrooms = row[5]
            house.no_of_bathrooms = row[6]
            house.floor_space = row[7]
            house.price = row[8]
            house.real_state_Desc = row[2]

        cursor.close()
        if(sellOrBuy == 1):
            house.SellRealState(house.price)
        else:
            house.BuyRealState(house.price)


def main():
    # clear()

    answer = input(
        "1- Sign in"
        "\n2- Sign up "
        "\n>>"
    )
    if answer[:1] == '1':
        clear()
        print("Succesful log in!")

        #Employee = Employee()

        # -----------------------------------------------
        # if I'm the system admin show this menue
        clear()
        print("--------------------------------------------------------------------------------")
        print("---------------------- WELCOME TO OUR ONLINE RETAIL STORE ----------------------")
        print("\n\n")

        print("                       ~~ MAIN MENUE ~~\n\n")

        print("                       1- Manage Categories")
        print("                       2- Manage Products")
        print("                       3- Manage Customers\n")
        answer = int(input("Please choose your option [1-3] >>"))
        clear()

        if answer[:1] == '1':
            print("Search Categories by CATEGORY NAME")
            SearchKeyWord = input("What you looking for? >>")
            SQLStatment = selectStatment(
                "categories", "LOWER(category_name) LIKE '" + SearchKeyWord + "%'")
            rows = retreiveDataFromDBTables(SQLStatment)

            # Retrive real state data from database
            print("-------------------------------------------------------------:")
            print("---------------------- Categories List ----------------------")
            ProductCategory = Category()

            if(rows):
                ProductCategoryList = rows
                for row in rows:
                    print(f"{row[0]} - {row[1]} ")

        elif answer[:1] == '2':
            # retreiveAllRealStates()
            # real_state_id = int(
            #     input("Please select which real state you want to sell >>"))
            # selectSpesificRealState(real_state_id, 1)
            print("Invalid entry\n")
        elif answer[:1] == '3':
            # retreiveAllRealStates()
            # real_state_id = int(
            #     input("Please select which real state you want to buy >>"))
            # selectSpesificRealState(real_state_id, 2)
            print("Invalid entry\n")
        else:
            print("Invalid entry\n")


clear()
main()
