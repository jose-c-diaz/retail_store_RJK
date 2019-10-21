import psycopg2


conn = psycopg2.connect(
    database="RetailStore",
    user="postgres",
    password="1234",
    host="127.0.0.1",
    port="5432"
)


class Customer:
    def __init__(self, CID=None, userIn=None, fName=None, lName=None, phone=None, emailaddress=None, Address=None, active=None, userId=None, Birthday=None):
        self.CID = CID
        self.userIn = userIn
        self.fName = fName
        self.lName = lName
        self.phone = phone
        self.emailaddress = emailaddress
        self.Address = Address
        self.active = active
        self.userId = userId
        self.Birthday = Birthday

    try:
        # Checks if username exists already
        def checkUsername(self, userIn):
            while True:
                newUserInput = input("\n\nEnter a unique username! >> ")

                cursor = conn.cursor()
                cursor.execute(
                    f"SELECT user_Name FROM user_authentication WHERE user_Name='{newUserInput}'")
                rows = cursor.fetchall()
                cursor.close()

                if rows:
                    print("Sorry! That username already exists! Let's try another one")
                else:
                    print("\nUsername available! Lets continue.\n")
                    break
            return newUserInput

    # This function checks whether the user is an admin or user, and if their account exists
        def retrieveCustomerInfo(self, userIn):
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM customers WHERE user_Name='{userIn}'")

            row = cursor.fetchall()
            if row:
                self.cid = row[0]
                print(row)
            else:
                print("User does not exist!")
            cursor.close()

    # This inserts the customer information into the database
        def insertCustomerInfo(self, userIn, fname, lname, phoneNumber, emailAddress, homeAddress, active, birthday):
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO customers (user_Name, fName, lName, phone, emailaddress, Address, active, Birthday) VALUES ('{userIn}', '{fname}', '{lname}', '{phoneNumber}','{emailAddress}','{homeAddress}','True','{birthday}')"
            )
            conn.commit()
            print("New Customer information saved!")
            cursor.close()

    except (Exception, psycopg2.Error):
        print("Error while fetching data frm your database")
