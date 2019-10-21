import psycopg2
import re
import os
from Categories import Categories


class Products:

    def __init__(self, product_id=None, category_id=None, product_name=None, product_desciption=None, product_price=None):

        self.product_id = product_id
        self.category_id = category_id
        self.product_name = product_name
        self.product_desciption = product_desciption
        self.product_price = product_price
    # Function to clear screen
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
    # This function to update products table in DB
    def retriveProductsGroupedByCategory(self):

        selcectSt = selectStatment(
            "category_id", "products", "GROUP BY category_id")
        result = self.executeSQLStatment(selcectSt)
        return result

    def EditProductTable(self, productNo, productOldName, productNewName, productDesc, productPrice):
        UpdateStatment = f"UPDATE products SET product_name=LOWER('{productNewName}'), product_desciption='{productDesc}', product_price='{productPrice}' WHERE product_id={productNo}"
        result = self.executeSQLStatment(UpdateStatment)
        if(result):
            print(
                f"\n\n{productOldName} is successfully updated!")

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
            return cursor

        except(Exception, psycopg2.Error)as err:
            self.clear()
            print("Error:", err)
    # Edit Existing Product
    # This function is to select all categories and products from db

    def retriveProductsOrderByCategory(self):
        selectSt = "SELECT c1.category_id, INITCAP(c1.category_name) as category_Name , c2.product_id, INITCAP(c2.product_name), c2.product_desciption, c2.product_price FROM categories c1 JOIN products c2 ON c1.category_id = c2.category_id ORDER BY category_Name ASC"
        result = self.executeSQLStatment(selectSt)
        return result

    def ValidateUserInputAsNumber(self, inputString):
        if not re.match("^[0-9 -]+$", inputString):
            return False
        else:
            return True

    def editExistingProduct(self, whereStatment):
        self.clear()
        product = Products()
        SQLStatment = product.selectStatment(
            "*", "products", whereStatment)
        cursor = self.executeSQLStatment(SQLStatment)
        rows = cursor.fetchall()
        cursor.close()
        print("-------------------------------------------------------------:")
        print("---------------------- Products List -------------------------")
        #ProductCategory = Category()
        if(rows):

            counter = 0
            for row in rows:

                print(f"{counter+1} - {row[2]} ")
                counter += 1
            productNo = input(
                "\n\nPlease enter a valid product from the list above>>")
            if product.ValidateUserInputAsNumber(productNo):
                productNo = int(productNo)
                if(productNo > 0 and productNo <= counter and productNo is not None):
                    rowIndex = int(productNo)-1
                    product_id = int(rows[rowIndex][0])
                    print("\n\n ***Edit Product Information:***")
                    productName = input(
                        "Please enter the product name >> ")
                    productDescription = input(
                        "Please enter the product description >> ")
                    productPrice = input(
                        "Please enter the product price >> ")
                    self.EditProductTable(
                        product_id, rows[rowIndex][2], productName, productDescription, productPrice)

    # Function to add new product
    def addNewProduct(self, category_id, product_name, product_desciption, product_price):

        insertstatment = f"INSERT INTO products (category_id, product_name, product_desciption, product_price) VALUES ('{category_id}',LOWER('{product_name}'),LOWER('{product_desciption}'),'{product_price}')"
        result = self.executeSQLStatment(insertstatment)

        if(result):

            print(f"\n\n{product_name} is successfully added to the system!")
    # Main menu items

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
        product = Products()
        self.clear()
        print("                    ***** Manage Products *****\n\n")
        print("                       1- Add a new product")
        print("                       2- Edit existing product")
        print("                       3- Remove existing product\n")
        productOperation = input("Please choose your option [1-3] >>")

        if productOperation[:1] == '1':
            category = Categories()
            self.clear()
            # Retrive real state data from database
            print("Options:")
            print(
                "\n\n1- Choose a category from the existing categories to add your product to")
            print("\n2- Add a new category to connect your product to")

            option = input("\nPlease make a selection [1-2] >>")
            if category.ValidateUserInputAsNumber(option):
                option = int(option)
                if(option == 1 or option == 2):
                    if(option == 1):
                        self.clear()

                        SQLStatment = category.selectStatment(
                            "*", "categories", "")
                        cursor = self.executeSQLStatment(SQLStatment)
                        rows = cursor.fetchall()
                        cursor.close()
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
                        categoryNo = input(
                            "\n\nPlease enter a valid category from the list above>>")
                        if category.ValidateUserInputAsNumber(categoryNo):
                            categoryNo = int(categoryNo)
                            if(categoryNo > 0 and categoryNo <= counter and categoryNo is not None):
                                rowIndex = int(categoryNo)-1
                                category_id = int(rows[rowIndex][0])
                                print("\n\n ***New Product Information:***")
                                productName = input(
                                    "Please enter the product name >> ")
                                productDescription = input(
                                    "Please enter the product description >> ")
                                productPrice = input(
                                    "Please enter the product price >> ")
                                self.addNewProduct(
                                    category_id, productName, productDescription, productPrice)

                    else:
                        categoryName = input(
                            "Please enter the Category name that you want to add >>")
                        rows = category.addNewCategory(categoryName)
                        category_id = rows.fetchone()[0]
                        print("\n\n ***New Product Information:***")
                        productName = input(
                            "Please enter the product name >> ")
                        productDescription = input(
                            "Please enter the product description >> ")
                        productPrice = input(
                            "Please enter the product price >> ")
                        self.addNewProduct(
                            category_id, productName, productDescription, productPrice)

                else:
                    print("invalid option")

        elif productOperation[:1] == '2':
            # self.EditProduct("Edit")
            # self.editExistingProduct(

            print("\n\n- Search Products by Name -")
            productName = input(
                "Please enter a keyword to search for Product Name >> ")
            whereStatment = f"LOWER(product_name) like '%{productName}%' "
            self.editExistingProduct(whereStatment)
        elif productOperation[:1] == '3':
            self.searchMainMenu("Delete")

        else:

            print("Invalid entry\n")
