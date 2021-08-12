from flaskr.models import User, ItemFlower
from flaskr import db


def select_user(username):
    return User.query.filter_by(username=username).first()


def select_flowers():
    return ItemFlower.query.all()


def select_flower(flower_id):
    return ItemFlower.query.filter_by(id=flower_id).first()


def update_flower(item):
    ItemFlower.query.filter_by(id=item['id']) \
        .update({
            ItemFlower.title: item['title'],
            ItemFlower.description: item['description'],
            ItemFlower.image_name: item['image_name'],
        })
    db.session.commit()


# def create_admin():
#     with open('.credentials', 'r') as f:
#         username, password = f.readline().split(':')
#
#     admin = User(username=username, password=hash_password(password))
#     db.session.add(admin)
#     db.session.commit()
