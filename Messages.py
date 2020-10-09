from vk_api.utils import get_random_id

import auth


def sendmsg(user,msg):
    auth.vk1.messages.send(
        user_id=user,
        random_id=get_random_id(),
        message=msg
    )
