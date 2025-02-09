from flask import Blueprint

us = Blueprint("user", __name__)

from . import routes