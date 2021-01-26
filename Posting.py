# -*- coding: utf-8 -*-
import logging

import Keyboard
import auth
from vk_api.bot_longpoll import VkBotEventType
import Messages
import main
import Balance
from auth import vk_post


def addpost(user,adm):
    Keyboard.back(user,"Что будем публиковать?")
    for event in auth.longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.obj.message['text'] == 'Назад':
                Keyboard.main(user,"Меню",adm)
                main.main()
            try:
                Messages.sendmsg(user,event.obj.message['text'])
            except Exception:
                Messages.sendmsg(user,'Не могу отправить картинку')
                Messages.sendmsg(user,
                                 "Давайте еще раз")
                addpost(user,adm)
            ad = (event.obj.message['text'])
            Keyboard.choose(user,"Всё верно?")
            for event in auth.longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    if event.obj.message['text'] == 'Да':
                        Messages.sendmsg(user,
                                         "Хорошо, публикую объявление! С вашего баланса будет списан пост.")
                        Balance.changebalance(user)
                        Messages.sendmsg(user,"Осталось "+str(Balance.GetUserData(user)[1]))
                        logging.info(f" Пользователь {user} опубликовал пост \n<{ad}>")
                        publish(ad)
                        Keyboard.main(user,"Меню",adm)
                        main.main()
                    elif event.obj.message['text'] == 'Нет':
                        Messages.sendmsg(user,
                                         "Давайте еще раз")
                        addpost(user,adm)
                    elif event.obj.message['text'] == 'Назад':
                        Keyboard.main(user,"Вернулся назад",adm)
                        main.main()


def publish(text):
    OWNER_ID = '-140216235'
    rs = vk_post.method('wall.post',{
        'owner_id': OWNER_ID,
        'message': str(text),
    })
    logging.info(f"Опубликован пост: {rs}")
