# flask-lightning
Ember lightning hosting for https://github.com/ember-cli/ember-cli-deploy written in Flask (http://flask.pocoo.org)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/dellintosh/flask-lightning)

The application expects these environment variables:

### `APP_NAME`

The name of the application as deployed in Redis.

### `REDIS_URL`

The Redis server url where ember-cli applications are deployed.  Uses the format defined at https://github.com/ddollar/redis-url
