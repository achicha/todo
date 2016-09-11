from flask import flash, redirect, render_template, request, \
     url_for, Blueprint
from flask_login import login_required, login_user, logout_user
from flask_bcrypt import generate_password_hash, check_password_hash

from .forms import LoginForm, RegisterForm
from .models import User
from ..database import db


bp_users = Blueprint(
    'users', __name__,
    template_folder='templates'
)  # pragma: no cover


# route for handling the login page logic
@bp_users.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and check_password_hash(user.password, request.form['password']):
                # session['logged_in'] = True
                login_user(user)
                flash('You were logged in.')
                return redirect(url_for('todo.todo_lst'))
            else:
                error = 'Invalid Credentials. Please try again.'

    return render_template('login.html', form=form, error=error)


@bp_users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('todo.todo_lst'))


@bp_users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('todo.todo_lst'))
    return render_template('register.html', form=form)
