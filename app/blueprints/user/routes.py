from . import us
from app.db import pool
from flask import jsonify

@us.route("/")
def index():
    with pool.connection() as conn:
        users = conn.execute("SELECT * FROM users;").fetchall()
        return jsonify({"users:": users})