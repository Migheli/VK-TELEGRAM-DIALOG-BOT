# -*- coding: cp1251 -*-

import os
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, Filters, MessageHandler, Updater
import logging.config
from loggers import LOGGING_CONFIG
from intents_detecters import detect_intent_texts_tg


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('telegram_logger')


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='����������� ����, �������!')


def dialogflow_conversation(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=detect_intent_texts_tg(os.getenv('DIALOG_FLOW_PROJECT_ID'),
                                                         os.getenv('SESSION_ID'),
                                                         update.message.text,
                                                         os.getenv('LANGUAGE_CODE')
                                                         )
                             )


def main():
    while True:
        try:
            updater = Updater(token=os.getenv('TG_BOT_TOKEN'))
            dispatcher = updater.dispatcher
            logger.debug('��� � Telegram ������� �������')
            dispatcher.add_handler(CommandHandler('start', start))
            dispatcher.add_handler(MessageHandler(Filters.text &
                                                  (~Filters.command),
                                                  dialogflow_conversation)
                                   )
            updater.start_polling()
            updater.idle()

        except Exception as err:
            logger.error('��� Telegram ���� �� ��������� �������:')
            logger.exception(err)


if __name__ == "__main__":
    main()
