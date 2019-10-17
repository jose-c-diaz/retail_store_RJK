
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


def retreiveDataFromDBTables(sqlStatment):
    try:
        conn = psycopg2.connect(
            database="RetailStore",
            user="postgres",
            password="6108",
            host="127.0.0.1",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute(sqlStatment)
        conn.commit()
        # cursor.close()
        return cursor

    except(Exception, psycopg2.Error)as err:
        clear()
        print("Error:", err)


def addNewCategory(CategoryName):
    insertstatment = f"INSERT INTO categories (category_name) VALUES ('{CategoryName}')"
    result = retreiveDataFromDBTables(insertstatment)
    if(result):
        print(f"\n\n{CategoryName} is successfully added to the system!")


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

        if answer[:1] == '1':
            print("                   ~~ Administration MAIN MENUE ~~\n\n")

            print("                       1- Manage Categories")
            print("                       2- Manage Products")
            print("                       3- Manage Customers\n")
            manageGRP = input("Please choose your option [1-3] >>")

            if manageGRP[:1] == '1':
                clear()
                print("                    ***** Manage Categories *****\n\n")
                print("                       1- Add a new category")
                print("                       2- Edit existing category")
                print("                       3- Remove existing category\n")
                categoryOperation = input("Please choose your option [1-3] >>")

                if categoryOperation[:1] == '1':
                    categoryName = input(
                        "Please enter the Category name that you want to add >>")
                    cursor = addNewCategory(categoryName)

                elif categoryOperation[:1] == '2':

                    print("Search Categories by CATEGORY NAME")
                    SearchKeyWord = str.lower(
                        input("What you looking for? >>"))
                    SQLStatment = selectStatment(
                        "categories", "LOWER(category_name) LIKE '" + SearchKeyWord + "%' ORDER BY category_name ASC")
                    cursor = retreiveDataFromDBTables(SQLStatment)
                    rows = cursor.fetchall()
                    cursor.close()
                    clear()
                    # Retrive real state data from database
                    print(
                        "-------------------------------------------------------------:")
                    print(
                        "---------------------- Categories List ----------------------")
                    ProductCategory = Category()

                    if(rows):
                        ProductCategoryList = rows
                        counter = 0
                        for row in rows:
                            print(f"{row[0]} - {row[1]} ")
                            counter += 1

                elif categoryOperation[:1] == '3':

                    print("Invalid entry\n")
                else:
                    print("Invalid entry\n")

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
