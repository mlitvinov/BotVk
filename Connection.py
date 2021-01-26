import mysql.connector
from mysql.connector import Error


def getcon():
    con = create_connection("localhost","admin","admin")
    return con

def create_connection(host_name,user_name,user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            db='bot'
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
