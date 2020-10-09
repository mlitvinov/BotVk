import vk_api
from vk_api.bot_longpoll import VkBotLongPoll

GROUP_ID = '140216235'
token = '8daa907027625ad9799f58abb05683b92db5842fb11d28823c07a255b1d986311837074dc00f03242e2bb'
token_post = 'c101c5f24d138bd4ba96e379d925c6dfef02099085371f84a9b3bd91b43b347382377e19b7e6768f00f28'
vk = vk_api.VkApi(token=token)
vk_post = vk_api.VkApi(token=token_post)

longpoll = VkBotLongPoll(vk,group_id=GROUP_ID)
vk_session = vk_api.VkApi(token=token)
vk1 = vk_session.get_api()
