from flaskr.models import User


def select_user(username):
    return User.query.filter_by(username=username).first()


# def create_admin():
#     with open('.credentials', 'r') as f:
#         username, password = f.readline().split(':')
#
#     admin = User(username=username, password=hash_password(password))
#     db.session.add(admin)
#     db.session.commit()
