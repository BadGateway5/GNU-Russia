from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.blueprints.user import us
app.register_blueprint(us)