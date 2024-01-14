import os
from .base import *

SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = False
ALLOWED_HOSTS = [] # TODO: Add your production host here

# will output to logging file
# Logging configuration
LOGGING_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)


# Rotate based on file size
# Write up to 10 MB, then rotate up to 5 files
MAX_LOG_SIZE = 1024*1024*10
BACKUP_COUNT = 5
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'django.log'),
            'filemode': 'a',
            'formatter': 'verbose',
            'maxBytes': MAX_LOG_SIZE,
            'backupCount': BACKUP_COUNT,
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'INFO',
    },
}
