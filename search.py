from mysql.connector import Error
from mysqlx import OperationalError

import Connection,search


def search(Tuple,n):
    for i in range(len(Tuple)):

        if Tuple[i] == n:
            return True

    return False

def execute_query(connection, query):
 connection.autocommit = True
 cursor = connection.cursor()
 try:
    cursor.execute(query)
    print("Query executed successfully")
 except OperationalError as e:
    print(f"The error '{e}' occurred")

def execute_read_query(connection,query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def findid(user_id):
    select_users = "SELECT ID FROM vip"
    users = execute_read_query(Connection.getcon(),select_users)
    for user in users:
        if search(user,user_id):
            return True
        else:
            return False
