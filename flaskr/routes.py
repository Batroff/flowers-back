from flask import request, render_template, redirect, url_for

from flask_login import login_user, login_required, logout_user
from flaskr.database_queries import select_user, select_flowers, update_flower, select_flower

from flaskr import blueprint
from flaskr.forms import LoginForm


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)

    if 'login' in request.form:
        username = request.form['username']
        password = request.form['password']

        user = select_user(username)

        if user and user.password == password:
            login_user(user)
            return redirect(url_for('base_blueprint.admin'))
        else:
            return render_template('login.html', form=login_form, msg='Логин или пароль введены неверно')

    return render_template('login.html', form=login_form)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    flowers = select_flowers()
    msg = None

    if 'apply' in request.form:

        for flower in flowers:
            if flower.title == request.form['title']:
                msg = 'Товар с таким именем уже существует'
            elif flower.image_name == request.form['image_name']:
                msg = 'Данное изображение уже существует'

        if msg is None:
            update_flower(request.form)
            msg = 'Успешно'

    elif 'delete':
        print(f'delete {request.form}')

    return render_template('admin.html', items=flowers, msg=msg)
