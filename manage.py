#!/usr/bin/env python
import os

from dotenv import Dotenv
from flask.ext.script import Manager

dotenv = Dotenv(os.path.join(os.path.dirname(__file__), '.env'))
os.environ.update(dotenv)
# Have to import the application AFTER the .env is parsed, above.
from lightning import wsgi

manager = Manager(wsgi.application)

if __name__ == "__main__":
    manager.run()
