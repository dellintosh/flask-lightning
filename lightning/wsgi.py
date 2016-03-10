import logging

from flask import Flask, Response, request
from flask.ext.redis import FlaskRedis

logger = logging.getLogger(__name__)


application = Flask(__name__)
application.config.from_pyfile('settings.py')
redis_store = FlaskRedis(application)


def _get_by_key(key='current'):
    project = application.config.get('PROJECT_NAME')
    return redis_store.get('{}:index:{}'.format(project, key))


@application.route('/')
def index():
    revision = request.args.get('revision')
    if not revision:
        revision = _get_by_key('current').decode()
    return get_revision(revision)


def get_revision(revision):
    return Response(_get_by_key(revision), mimetype='text/html')
