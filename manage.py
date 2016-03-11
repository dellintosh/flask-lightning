#!/usr/bin/env python
import os

from dotenv import Dotenv
from flask import redirect
from flask.ext.script import Manager

dotenv = Dotenv(os.path.join(os.path.dirname(__file__), '.env'))
os.environ.update(dotenv)
# Have to import the application AFTER the .env is parsed, above.
from lightning.wsgi import application


# This route is ONLY for local development, and requires the
# 'STATIC_FILES_URI' environment variable being set to a static file
# server that is hosting the (current) assets... those assets that
# the index.html file is trying to load.  It should _probably_ be
# contained in a separate module that gets loaded but this is the
# quickest way to get this working.
@application.route('/assets/<asset>', defaults={'asset_type': 'assets'})
def asset(asset_type, asset):
    return redirect('{static_files_uri}/{asset_type}/{asset}'.format(
        static_files_uri=application.config.get('STATIC_FILES_URI'),
        asset_type=asset_type,
        asset=asset
    ))

manager = Manager(application)

if __name__ == "__main__":
    manager.run()
