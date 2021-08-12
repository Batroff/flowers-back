from flask_login import UserMixin

from flaskr import db, login_manager
from sqlalchemy import Integer, String, LargeBinary, Column


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(60), unique=True, nullable=False)
    # password = Column(LargeBinary, nullable=False)
    password = Column(String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username,
        self.password = password

    def __repr__(self):
        return '<User id={}, username={}, password={}/>' \
            .format(self.id, self.username, self.password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class ItemFlower(db.Model):
    __tablename__ = 'flowers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False, unique=True)
    description = Column(String(200))
    image_name = Column(String(200), nullable=False, unique=True)

    def __init__(self, title, description, image_name):
        self.title = title
        self.description = description
        self.image_name = image_name

    def __repr__(self):
        return '<ItemFlower id={}, title={}, description={}, image_name={}/>'\
            .format(self.id, self.title, self.description, self.image_name)
