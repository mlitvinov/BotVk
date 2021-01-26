# -*- coding: utf-8 -*-
import logging

import Admin
import Balance
import Keyboard
import Posting
import auth
from vk_api.bot_longpoll import VkBotEventType
import Messages


def main():
    for event in auth.longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            user = event.obj.message["from_id"]
            if Balance.GetUserData(user) is not None:
                adm = Balance.GetUserData(user)[0]
                balance = Balance.GetUserData(user)[1]
            elif Balance.GetUserData(user) is None:
                Admin.addUser(user)
                balance = Balance.GetUserData(user)[1]
                adm = Balance.GetUserData(user)[0]
            Keyboard.main(user,"Меню",adm)
            if event.obj.message['text'] != '':
                if event.obj.message['text'] == 'Опубликовать':
                    if event.from_user and balance > 0:
                        Posting.addpost(user,adm)
                    elif balance == 0:
                        Messages.sendmsg(user,"Баланс пуст. Осталось "+str(balance))
                if event.obj.message['text'] == 'Баланс':
                    Messages.sendmsg(user,"Осталось "+str(balance))
                if event.obj.message['text'] == 'Назначить/Снять админа':
                    Keyboard.back(user,"Введите ID пользователя")
                    for event in auth.longpoll.listen():
                        if event.type == VkBotEventType.MESSAGE_NEW:
                            if event.obj.message['text'] == 'Назад':
                                Keyboard.main(user,"Меню",adm)
                                main()
                            try:
                                adminID = int(event.obj.message['text'])
                            except Exception:
                                Messages.sendmsg(user,"Используйте цифры")
                                continue
                            Keyboard.role(user,"Что сделать с пользователем?")
                            for event in auth.longpoll.listen():
                                if event.type == VkBotEventType.MESSAGE_NEW:
                                    if event.obj.message['text'] == 'Назначить':
                                        Admin.updateRole(1,adminID,user)
                                        Messages.sendmsg(user,"Готово")
                                    elif event.obj.message['text'] == 'Отстранить':
                                        Admin.updateRole(0,adminID,user)
                                        Messages.sendmsg(user,"Готово")
                                    if event.obj.message['text'] == 'Назад':
                                        Keyboard.main(user,"Меню",adm)
                                        main()

                if event.obj.message['text'] == 'Указать количество постов' and adm == 1:
                    Keyboard.back(user,"Сколько постов хотите?")
                    for event in auth.longpoll.listen():
                        if event.type == VkBotEventType.MESSAGE_NEW:
                            if event.obj.message['text'] == 'Назад':
                                Keyboard.main(user,"Меню",adm)
                                main()
                            try:
                                Balance.updatebalance(int(event.obj.message['text']),user,user)
                                Messages.sendmsg(user,
                                                 "Теперь на этом аккаунте "+str(event.obj.message['text'])+" постов")
                                main()
                            except ValueError as e:
                                Messages.sendmsg(user,"Введите число")
                                print(e)


if __name__ == '__main__':
    logging.basicConfig(filename="logs.log",level=logging.INFO,filemode="w")
    logging.info("Informational message")
    logging.error("An error has happened!")
    main()
