from . import us
from flask import request, render_template, redirect, url_for, session
from .forms import LoginForm
from app.repositories.user_repository import User
from .utils import login_required

user = User()


@us.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect(url_for('us.login'))


@us.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        is_user = user.get_user(login, password)
        if is_user:
            session['user_info'] = is_user
            return redirect(url_for("us.index"))
    return render_template("auth/login.html", form=form)


@us.route("/")
@login_required
def index():
    logout_link = url_for('us.logout')
    return f"""Hello {session['user_info'][1]}!
            <a href={logout_link}>Выйти</a>"""
