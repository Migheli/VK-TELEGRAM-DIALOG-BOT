from logging import Handler, LogRecord
import telegram


class TelegramLogsHandler(Handler):

    def __init__(self, token, chat_id):
        super().__init__()
        self.token = token
        self.chat_id = chat_id

    def emit(self, record: LogRecord):
        bot = telegram.Bot(self.token)
        log_entry = self.format(record)
        bot.send_message(chat_id=self.chat_id, text=log_entry)
