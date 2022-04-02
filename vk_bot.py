# -*- coding: cp1251 -*-

import os
import random
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
import logging.config
from intents_detecters import detect_intent_texts_vk
from loggers import LOGGING_CONFIG


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('telegram_logger')


def dialogflow_conversation(event, vk_api):

    event_txt = detect_intent_texts_vk(os.getenv('DIALOG_FLOW_PROJECT_ID'),
                                       os.getenv('TG_CHAT_ID'),
                                       event.text,
                                       os.getenv('LANGUAGE_CODE')
                                       )

    if event_txt:

        vk_api.messages.send(
            user_id=event.user_id,
            message=event_txt,
            random_id=random.randint(1, 1000)
        )


def main():
    while True:
        try:
            vk_group_access_key = os.getenv('VK_GROUP_ACCESS_KEY')
            vk_session = vk.VkApi(token=vk_group_access_key)
            logger.debug('Бот Вконтакте успешно запущен')
            vk_api = vk_session.get_api()
            longpoll = VkLongPoll(vk_session)
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    dialogflow_conversation(event, vk_api)

        except Exception as err:
            logger.error('Бот Вконтакте со следующей ошибкой:')
            logger.exception(err)


if __name__ == "__main__":
    main()
