import os

DEBUG = os.environ.get('DEBUG', False)

PROJECT_NAME = os.environ.get('PROJECT_NAME', 'lightning')
REDIS_URL = os.environ.get('REDIS_URL', 'redis://:password@localhost:6379/0')
