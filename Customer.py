import psycopg2

conn = psycopg2.connect(
    database="RetailStore",
    user="postgres",
    password="45928",
    host="127.0.0.1",
    port="5432"
)


class Customer:
    def __init__(self, CID=None, fName=None, lName=None, phone=None, emailaddress=None, Address=None, active=None, Birthday=None):
        self.CID = CID
        self.fName = fName
        self.lName = lName
        self.phone = phone
        self.emailaddress = emailaddress
        self.Address = Address
        self.active = active
        self.Birthday = Birthday

    # This establishes the connection to PG
    try:

        # This function is suppose to make the user authen table on the PG Database
        def createCustomerTable():
            cursor = conn.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS customers
                    (
                        
                        CID SERIAL PRIMARY KEY,
                        user_id text NOT NULL,
                        fName text NOT NULL,
                        lName text NOT NULL,
                        phone text NOT NULL,
                        email_address text NOT NULL,
                        address text NOT NULL,
                        active boolean  NOT NULL,
                        Birthday date
                    )
                """
            )
            conn.commit()
            cursor.close()

        createCustomerTable()

        # This function checks whether the user is an admin or user, and if their account exists

        def retrieveCustomerInfo(self, user_id):
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM customers WHERE user_id='{user_id}'")
            # rows = cursor.fetchall()
            row = cursor.fetchall()

            if row:
                self.cid = row[0]
                print(row)
            else:
                print("User does not exist!")
            # else:
            #     print("User does not exist")
            cursor.close()
        
        def insertCustomerInfo(self, userID, fname, lname, phoneNumber, emailAddress, homeAddress, birthday):
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO customers (user_id, fName, lName, phone, email_address, address, Birthday, active) VALUES ('{userID}', '{fname}', '{lname}', '{phoneNumber}','{emailAddress}','{homeAddress}','{birthday}','true')"
            )
            conn.commit()
            print("Customer information saved!")
            cursor.close()

    except (Exception, psycopg2.Error):
        print("Error while fetching data frm your database")
