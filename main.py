import psycopg2
from UserAuth import UserAuth

try:
    conn = psycopg2.connect(
        database="RetailStore",
        user="postgres",
        password="6108",
        host="127.0.0.1",
        port="5432"
    )

except(Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

UserAuth = UserAuth()
# UserAuth.username = input("Enter your username >> ")
# function.actions(UserAuth.fname, UserAuth.lname, "username")
# user.password = input("Enter your password >> ")
# function.actions(UserAuth.fname, UserAuth.lname, "")
# if(UserAuth.username == username and user.password == password):
#     print("User has been authenticated")
# else:
#     print("Wrong credentials")
