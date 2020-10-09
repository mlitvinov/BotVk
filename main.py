# -*- coding: utf-8 -*-
import Admin
import Balance
import Keyboard
import Posting
import auth
from vk_api.bot_longpoll import VkBotEventType
import Messages
import search

def main():
    for event in auth.longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            user = event.obj.message["from_id"]
            try:
                balance = Balance.getuserdata(user)[1]
            except Exception:
                Admin.addUser(user)
                balance = Balance.getuserdata(user)[1]

            Keyboard.main(user,"Меню")
            if event.obj.message['text'] != '':
                if event.obj.message['text'] == 'Опубликовать':
                    if event.from_user and search.findid(user) and balance > 0:
                        Posting.addpost(user)
                    elif balance == 0:
                        Messages.sendmsg(user,"Баланс пуст. Осталось " + str(balance))
                    elif not search.findid(user):
                        Messages.sendmsg(user,"Вас нет в списке пользователей оплативших услугу")
                if event.obj.message['text'] == 'Баланс':
                    Messages.sendmsg(user,"Осталось "+str(balance))
                if event.obj.message['text'] == 'Указать количество постов':
                    Keyboard.back(user,"Сколько постов хотите?")
                    for event in auth.longpoll.listen():
                        if event.type == VkBotEventType.MESSAGE_NEW:
                            if event.obj.message['text'] == 'Назад':
                                Keyboard.main(user,"Меню")
                                main()
                            try:
                                Balance.updatebalance(int(event.obj.message['text']),user)
                                Messages.sendmsg(user,"Теперь на этом аккаунте "+str(event.obj.message['text'])+" постов")
                                main()
                            except Exception as e:
                                Messages.sendmsg(user,"Введите число")
                                print(e)


if __name__ == '__main__':
    main()
