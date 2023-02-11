from flask.cli import FlaskGroup
from project import app

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli() # Starts the app
# So we use manage.py to start the app and not __init__.py
