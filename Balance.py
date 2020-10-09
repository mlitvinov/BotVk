import Connection,search


def getuserdata(users_id):

    """Функция getuserdata получает user_id, далее загружает по нему данные
    из БД в переменную data. После этого данные загружаются двумя for'ами
    в список user_info, а оттуда по 3 значения в словарь. Последний for
    выполняет поиск по словарю"""

    a = 0
    dic = {}  # Словарь для удобной работы с данными из БД
    users_info = []  # Список для первой загрузки данных
    select_data = "SELECT * FROM vip"
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


def updatebalance(x,user_id):
    update_balance = """
    UPDATE
     vip
    SET
     balance = %i
    WHERE
     id = %s
    """ % (x,user_id)

    search.execute_query(Connection.getcon(),update_balance)


def changebalance(user_id):
    changebalance = """
    
    UPDATE
     vip
    SET
     balance = balance - 1
    WHERE
     id = %s
    """ % (user_id)

    search.execute_query(Connection.getcon(),changebalance)


