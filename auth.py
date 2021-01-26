import vk_api
from vk_api.bot_longpoll import VkBotLongPoll

GROUP_ID = ''
token = ''
token_post = ''
vk = vk_api.VkApi(token=token)
vk_post = vk_api.VkApi(token=token_post)

longpoll = VkBotLongPoll(vk,group_id=GROUP_ID)
vk_session = vk_api.VkApi(token=token)
vk1 = vk_session.get_api()
