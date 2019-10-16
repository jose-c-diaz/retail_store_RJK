import psycopg2
import getpass


# This establishes the connection to PG
try:
    conn = psycopg2.connect(
        database="RetailStore",
        user="postgres",
        password="45928",
        host="127.0.0.1",
        port="5432"
    )

# This function is suppose to make the user authen table on the PG Database
    def createUserTable():
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS user_authentication
                (
                    user_id SERIAL PRIMARY KEY,
                    user_name TEXT NOT NULL,
                    pass_word TEXT NOT NULL,
                    admin_role BOOLEAN NOT NULL
                )
            """
        )
        conn.commit()
        cursor.close()
    createUserTable()

# This function  is suppose to insert the info into the user authen table
# the crypt() is suppose to hash the password once its inserted into the table
    def insertUserInfo(user, passW):
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO user_authentication (user_name, pass_word, admin_role) VALUES ('{user}', '{passW}', 'false')"
        )
        conn.commit()
        print("New User registered successfully!")
        cursor.close()


# This function checks whether the user is an admin or user, and if their account exists


    def retrieveAllUserInfo(user, passW, role):
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM user_authentication WHERE user_name='{user}' AND pass_word='{passW}' AND admin_role='{role}'")
        # rows = cursor.fetchall()
        row = cursor.fetchall()

        if row:
            if(role == 'true'):
                print(f"{user}, you have been authenticated. You're an admnistrator")
            elif(role == 'false'):
                print(f"{user}, you have been authenticated. You're a user")

        else:
            print("User does not exist!")
        # else:
        #     print("User does not exist")
        cursor.close()


except (Exception, psycopg2.Error) as error:
    print("Error while fetching data frm your database", error)
