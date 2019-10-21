import psycopg2
import re
import os


class Categories:

    def __init__(self, category_id=None, category_name=None):

        self.category_id = category_id
        self.category_name = category_name

    def clear(self): return os.system('cls')


# This function is to build dynamic select statment

    def selectStatment(self, coulmn, tableName, WhereStatment):

        if (WhereStatment != ""):
            selectStatment = "SELECT " + coulmn + " FROM " + \
                tableName + " WHERE " + WhereStatment
        else:
            selectStatment = "SELECT " + coulmn + " FROM " + \
                tableName

        return selectStatment

    # This function to Execute the sql command and return the data set

    def executeSQLStatment(self, sqlStatment):

        try:

            conn = psycopg2.connect(

                database="RetailStore",

                user="postgres",

                password="pcloud2019",

                host="127.0.0.1",

                port="5432"

            )

            cursor = conn.cursor()

            cursor.execute(sqlStatment)

            conn.commit()

            # cursor.close()

            return cursor

        except(Exception, psycopg2.Error)as err:

            self.clear()

            print("Error:", err)

    def addNewCategory(self, CategoryName):

        insertstatment = f"INSERT INTO categories (category_name) VALUES (LOWER('{CategoryName}')) RETURNING category_id"

        result = self.executeSQLStatment(insertstatment)

        if(result):

            print(f"\n\n{CategoryName} is successfully added to the system!")
        return result

    def EditCategory(self, categoryNo, CategoryOldName, categoryNewName):
        UpdateStatment = f"UPDATE categories SET category_name=LOWER('{categoryNewName}') WHERE category_id={categoryNo}"
        result = self.executeSQLStatment(UpdateStatment)
        if(result):
            print(
                f"\n\n{CategoryOldName} is successfully updated to {categoryNewName}!")

    def deleteCategory(self, categoryNo, CategoryOldName):
        deletestatment = f"DELETE FROM categories WHERE category_id={categoryNo}"

        result = self.executeSQLStatment(deletestatment)
        if(result):

            print(
                f"\n\n{CategoryOldName} is successfully deleted from the system!")

    def ValidateUserInputAsNumber(self, inputString):
        if not re.match("^[0-9 -]+$", inputString):
            return False
        else:
            return True

    def SearchCategories(self, operation, rows, counter):
        categoryNo = input(
            "\n\nPlease enter a valid category from the list >>")
        if self.ValidateUserInputAsNumber(categoryNo):
            categoryNo = int(categoryNo)
            if(categoryNo > 0 and categoryNo <= counter and categoryNo is not None):
                rowIndex = int(categoryNo)-1
                if(operation == "Edit"):
                    CategoryNewName = input(
                        "Please Enter the category new name  >>")

                    cursor = self.EditCategory(
                        int(rows[rowIndex][0]), rows[rowIndex][1], CategoryNewName)
                    return False
                else:

                    whileLoopFlag = True
                    while(whileLoopFlag):
                        confirmDelete = input(
                            f"Are you sure you want to delete (( {rows[rowIndex][1]} ))  Y|N>>")
                        if(str.upper(confirmDelete) == "YES" or str.upper(confirmDelete) == "NO" or str.upper(confirmDelete) == "Y" or str.upper(confirmDelete) == "N"):
                            if(str.upper(confirmDelete) == "YES" or str.upper(confirmDelete) == "Y"):

                                cursor = self.deleteCategory(
                                    rows[rowIndex][0], rows[rowIndex][1])
                                whileLoopFlag = False
                                return False
                            else:
                                return False
                        else:
                            whileLoopFlag = True

        else:
            self.SearchCategories(rows, counter)
            return True

    def searchMainMenu(self, operation):
        print("Search Categories by CATEGORY NAME")
        SearchKeyWord = str.lower(
            input("What you looking for? >>"))
        SQLStatment = self.selectStatment("category_id,INITCAP(category_name)",
                                          "categories", "LOWER(category_name) LIKE '%" + SearchKeyWord + "%' ORDER BY category_name ASC")
        cursor = self.executeSQLStatment(SQLStatment)
        rows = cursor.fetchall()
        cursor.close()
        self.clear()
        # Retrive real state data from database
        print(
            "-------------------------------------------------------------:")

        print(

            "---------------------- Categories List ----------------------")
        #ProductCategory = Category()
        if(rows):

            counter = 0
            for row in rows:

                print(f"{counter+1} - {row[1]} ")
                counter += 1

            whileFlag = True
            while(whileFlag):
                try:
                    if(operation == "Edit"):
                        whileFlag = self.SearchCategories(
                            "Edit", rows, counter)
                    else:
                        whileFlag = self.SearchCategories(
                            "Delete", rows, counter)
                except:
                    if(operation == "Edit"):
                        whileFlag = self.SearchCategories(
                            "Edit", rows, counter)
                    else:
                        whileFlag = self.SearchCategories(
                            "Delete", rows, counter)

    def main(self):
        category = Categories()
        self.clear()
        print("                    ***** Manage Categories *****\n\n")
        print("                       1- Add a new category")
        print("                       2- Edit existing category")
        print("                       3- Remove existing category\n")
        categoryOperation = input("Please choose your option [1-3] >>")

        if categoryOperation[:1] == '1':
            categoryName = input(
                "Please enter the Category name that you want to add >>")
            cursor = self.addNewCategory(categoryName)
        elif categoryOperation[:1] == '2':
            self.searchMainMenu("Edit")

        elif categoryOperation[:1] == '3':
            self.searchMainMenu("Delete")

        else:

            print("Invalid entry\n")
