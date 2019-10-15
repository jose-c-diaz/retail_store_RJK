import getpass
import os
import binascii
import hashlib
import psycopg2


class User:

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def Create_user_Account(self):
        print("\nLets register you")
        user = User()
        user.username = input("Username: ").lower()
        user.password = getpass.getpass("Enter your password: ")
        user.password = hash_password(user.password)

        csvfile = open('authentication.csv', 'a+')
        csvfile.write(f"{user.username},{user.password}\n")
        csvfile.close()

    def log_in(self):
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
        print(self.username)
        # Retrive user login info from database
        print("Log in info:")
        cursor = conn.cursor()

        cursor.execute(
            f"select * from userauth where user_name='{self.username}'")
        rows = cursor.fetchall()
        if(rows):
            if(self.password == rows[2]):
                print(f"{self.username}, you have been authinticated.")
            else:
                print(f"Wrong password!")
        else:
            print("User does not exist!")

        cursor.close()

    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password
