from flask.cli import FlaskGroup
from project import app, db
from project.models import User

cli = FlaskGroup(app)

@cli.command('create_db')
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    db.session.add(User(email="imasiftoo@gmail.com"))
    db.session.commit()

if __name__ == '__main__':
    cli() # Starts the app  
# So we use manage.py to start the app and not __init__.py