from . import db

#  User Model
class User(db.Model):
    __tablename__ = "mytable"

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email