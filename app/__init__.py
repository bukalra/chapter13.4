""" from flask import Flask    # 1
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)      # 2
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config["SECRET_KEY"] = "nininini" """

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask    # 1

app = Flask(__name__)      # 2
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config["SECRET_KEY"] = "nininini"

from app import routes, models