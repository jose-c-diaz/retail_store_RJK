import psycopg2
import getpass
import hashlib
import binascii
import os


# This establishes the connection to PG
try:
    conn = psycopg2.connect(
        database="RetailStore",
        user="postgres",
        password="1234",
        host="127.0.0.1",
        port="5432"
    )


# This creates the hash for the password

    def hash_password(passW):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', passW.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')


# This verifies the input password and hashed password match

    def verify_password(stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password


# This function  is suppose to insert the info into the user authen table

    def insertUserInfo(user, passW):
        passW = hash_password(passW)
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO user_authentication (user_Name, pass_word, admin_role) VALUES ('{user}', '{passW}', 'false')"
        )
        conn.commit()
        print("New User registered successfully!")
        cursor.close()


# This function checks whether the user is an admin or user, and if their account exists

    def retrieveAllUserInfo(user, passW, role):
        while True:
            userNameInput = input("\nEnter your username >> ")
            passwordInput = getpass.getpass("\nEnter your password >> ")
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM user_authentication WHERE user_Name='{userNameInput}' AND admin_role='{role}'")
            row = cursor.fetchall()
            cursor.close()
            passhash = verify_password(row[0][2], passwordInput)

            if row and passhash:
                if(role == 'true'):
                    print("\n~~~~~~~~~~~Succesful log in!~~~~~~~~~~~")
                    print(
                        f"\n\nWelcome {userNameInput} administrator! What would you like to do? ")
                    break
                elif(role == 'false'):
                    print("\n~~~~~~~~~~~Succesful log in!~~~~~~~~~~~")
                    print(
                        f"\n\nWelcome {userNameInput}, what would you like to do today? ")
                    break
            else:
                print(
                    "Incorrect username and/or password, please check your credentials!")
            return userNameInput, passwordInput


except (Exception, psycopg2.Error) as error:
    print("Error while fetching data frm your database", error)
