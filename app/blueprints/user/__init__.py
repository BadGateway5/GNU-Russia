from flask import Blueprint

us = Blueprint("us", __name__)

from . import routes