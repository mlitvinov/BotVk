# -*- coding: utf-8 -*-
from vk_api.keyboard import VkKeyboard,VkKeyboardColor
from vk_api.utils import get_random_id

import auth

vk = auth.vk.get_api()


def main(user_id,msg,adm):
    """ Пример создания клавиатуры для отправки ботом """
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Баланс',color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Опубликовать',color=VkKeyboardColor.POSITIVE)

    if adm == 1:
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Указать количество постов',color=VkKeyboardColor.SECONDARY)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Назначить/Снять админа',color=VkKeyboardColor.SECONDARY)
    # keyboard.add_location_button()

    keyboard.add_line()
    keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=140216235")



    vk.messages.send(
        peer_id=user_id,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message=msg
        # message="&#4448;"
    )


def choose(user_id,msg):
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Нет',color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Да',color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()  # Переход на вторую строку
    keyboard.add_button('Назад',color=VkKeyboardColor.SECONDARY)

    keyboard.add_line()

    keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=140216235")

    vk.messages.send(
        peer_id=user_id,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message=msg
    )


def back(user_id,msg):
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button('Назад',color=VkKeyboardColor.SECONDARY)

    vk.messages.send(
        peer_id=user_id,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message=msg
    )

def role(user_id,msg):
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Отстранить',color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Назначить',color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()  # Переход на вторую строку
    keyboard.add_button('Назад',color=VkKeyboardColor.SECONDARY)

    vk.messages.send(
        peer_id=user_id,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message=msg
    )


if __name__ == '__main__':
    main()
