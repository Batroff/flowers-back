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

