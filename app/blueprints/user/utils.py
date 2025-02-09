from flask import session, url_for, redirect
from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user_info" not in session:
            # Перенаправление на страницу логина с учетом Blueprint
            return redirect(url_for("us.login"))  # Здесь "us" — это имя вашего Blueprint
        return func(*args, **kwargs)
    return wrapper