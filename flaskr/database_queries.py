from flaskr.models import User, ItemFlower
from flaskr import db


def select_user(username):
    return User.query.filter_by(username=username).first()


def select_flowers():
    return ItemFlower.query.all()


def select_flower(item_id):
    return ItemFlower.query.filter_by(id=item_id).one_or_none()


def update_flower(item_dict):
    ItemFlower.query.filter_by(id=item_dict['id']) \
        .update({
            ItemFlower.title: item_dict['title'],
            ItemFlower.description: item_dict['description'],
            ItemFlower.image_name: item_dict['image_name'],
        })
    db.session.commit()


def delete_flower(item_id):
    ItemFlower.query.filter_by(id=item_id).delete()
    db.session.commit()


def add_flower(item_dict):
    flower = ItemFlower(title=item_dict['title'],
                        description=item_dict['description'],
                        image_name=item_dict['image_name'])
    db.session.add(flower)
    db.session.commit()

# def create_admin():
#     with open('.credentials', 'r') as f:
#         username, password = f.readline().split(':')
#
#     admin = User(username=username, password=hash_password(password))
#     db.session.add(admin)
#     db.session.commit()
