import os

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'default_formatter': {
            'format': '[%(name)s:%(levelname)s:%(asctime)s] %(message)s'
        },
    },
    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default_formatter',
        },
        'telegram_handler': {
            'class': 'handlers.TelegramLogsHandler',
            'formatter': 'default_formatter',
            'token': os.getenv('TG_BOT_TOKEN'),
            'chat_id': os.getenv('SESSION_ID')
        },
    },

    'loggers': {
        'telegram_logger': {
            'handlers': ['telegram_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'stream_logger': {
            'handlers': ['stream_handler'],
            'level': 'DEBUG',
            'propagate': True
        }
    },
    'root': {
        'handlers': ['stream_handler'],
        'level': 'DEBUG',
        'disable_existing_loggers': False,
    }
}
