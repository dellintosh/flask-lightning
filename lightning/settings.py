import os

DEBUG = os.environ.get('DEBUG', False)

APP_NAME = os.environ.get('APP_NAME', 'lightning')
REDIS_URL = os.environ.get('REDIS_URL', 'redis://:password@localhost:6379/0')
STATIC_FILES_URI = os.environ.get('STATIC_FILES_URI', 'http://localhost/static/')
