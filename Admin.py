import Connection
import search



def addUser(user_id):

    addUser = """
    INSERT INTO
     `vip`(`ID`,`vip`)
    VALUES 
     ('%i','0')
    """ % (user_id)

    search.execute_query(Connection.getcon(),addUser)

