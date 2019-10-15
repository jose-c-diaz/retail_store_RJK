import psycopg2

Username = ""
Password = ""
try:
    conn = psycopg2.connect(
        database="RetailStore",
        user="postgres",
        password="6108",
        host="127.0.0.1",
        port="5432"
    )

    def retriveAllUserInfo():
        cursor = conn.cursor()
        cursor.execute("select * from userauth")
        rows = cursor.fetchall()
        if(rows):
            for row in rows:

                Username = row[0]
                Password = row[1]

                cursor.close()

except(Exception, psycopg2.Error)as error:
    print("Error while fetching data from PostgreSQL", error)

retriveAllUserInfo()
userNameInput = input("Enter user name >>")
passwordInput = input("Enter password >>")

# if(userNameInput == Username and passwordInput == Password)
