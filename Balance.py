import Connection,search

import logging


def GetUserData(users_id):
    """Функция GetUserData получает user_id, далее загружает по нему данные
    из БД в переменную data. После этого данные загружаются двумя for'ами
    в список user_info, а оттуда по 3 значения в словарь. Последний for
    выполняет поиск по словарю"""

    a = 0
    dic = {}  # Словарь для удобной работы с данными из БД
    users_info = []  # Список для первой загрузки данных
    select_data = "SELECT * FROM `table`"
    data = search.execute_read_query(Connection.getcon(),select_data)

    for i in data:
        for j in i:
            users_info.append(j)
    length = int(len(users_info) / 3)

    for i in range(0,length):
        dic[users_info[a]] = [users_info[a+1],users_info[a+2]]
        a += 3

    for key,value in dic.items():
        if key == users_id:
            return value

def updatebalance(x,user_id,FromUser):
    update_balance = """
    UPDATE
     `table`
    SET
     balance = %i
    WHERE
     id = %s
    """ % (x,user_id)
    logging.info(f" Админ {FromUser} указал баланс пользователю {user_id} равный {x}")
    search.execute_query(Connection.getcon(),update_balance)


def changebalance(user_id):
    changebalance = """
    
    UPDATE
     `table`
    SET
     balance = balance - 1
    WHERE
     id = %s
    """ % (user_id)
    logging.info(f"Баланс {user_id} уменьшился на 1")
    search.execute_query(Connection.getcon(),changebalance)
