import logging

import Connection
import search


def addUser(user_id):
    addUser = """
    INSERT INTO
     `table`(`ID`,admin)
    VALUES 
     ('%i','0')
    """ % (user_id)
    logging.info(f"Пользователь {user_id} добавлен в базу данных")
    search.execute_query(Connection.getcon(),addUser)


def updateRole(x,user_id,FromUser):
    addUser = """
    UPDATE
     `table`
    SET
     admin = %i
    WHERE
     id = %s
    """ % (x,user_id)
    if x == 1:
        logging.info(f" Админ {FromUser} назначил {user_id} админом")
    elif x == 0:
        logging.info(f" Админ {FromUser} снял {user_id} с должности админа")
    search.execute_query(Connection.getcon(),addUser)
