from flask import request, render_template, redirect, url_for

from flask_login import login_user, login_required, logout_user
from flaskr.database_queries import select_user

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


@blueprint.route('/admin')
@login_required
def admin():
    return render_template('admin.html')
