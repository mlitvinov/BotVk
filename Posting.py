# -*- coding: utf-8 -*-
import Keyboard
import auth
from vk_api.bot_longpoll import VkBotEventType
import Messages
import main
import Balance


def addpost(user):
    Messages.sendmsg(user,"Что будем публиковать?")
    for event in auth.longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            Messages.sendmsg(user,event.obj.message['text'])
            Keyboard.choose(user,"Всё верно?")
            for event in auth.longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    if event.obj.message['text'] == 'Да':
                        Messages.sendmsg(user,
                                         "Хорошо, публикую объявление! С вашего баланса будет списан пост.")
                        Balance.changebalance(user)
                        Messages.sendmsg(user,"Осталось "+str(Balance.getuserdata(user)[1]))
                        Keyboard.main(user,"")
                        main.main()
                    elif event.obj.message['text'] == 'Нет':
                        Messages.sendmsg(user,
                                         "Давайте еще раз")
                        addpost(user)
                    elif event.obj.message['text'] == 'Назад':
                        Messages.sendmsg(user,
                                         "Вернулся назад")
                        main()


def postbybot():
    groupId = 140216235
    textPost = "sssss"
    auth.vk_post.method("wall.post",{
        "owner_id": groupId,
        "message": textPost,
        "copyright": copyright

    })


