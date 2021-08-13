from flask import request, render_template, redirect, url_for

from flask_login import login_user, login_required, logout_user
from flaskr.database_queries import select_user, select_flowers, update_flower, select_flower, add_flower, delete_flower

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

    print(request.form)
    if 'apply' in request.form:

        if msg is None:
            update_flower(request.form)
            msg = 'Успешно'

    elif 'add' in request.form:
        title = request.form['title']
        image_name = request.form['image_name']

        for flower in flowers:
            if flower.title == title:
                msg = 'Товар с таким именем уже существует'
            elif flower.image_name == image_name:
                msg = 'Данное изображение уже существует'

        if title == '' or image_name == '':
            msg = 'Поля "Название" и "Изображение" не могут быть пустыми'

        if msg is None:
            add_flower(request.form)
            msg = 'Успешно'

    elif 'delete' in request.form:
        item_id = request.form['id']

        if select_flower(item_id) is None:
            msg = 'Данного товара не существует'

        if msg is None:
            delete_flower(request.form)
            msg = f'Успешно удалён товар №{item_id}'

    return render_template('admin.html', items=flowers, msg=msg)
