from flask import Flask
from flask import render_template

from src.common.database import Database

app = Flask(__name__)
app.config.from_object('src.config')
app.secret_key = "123"

from src.models.users.views import user_blueprint
from src.models.diagrams.views import diagram_blueprint

app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(diagram_blueprint, url_prefix="/diagrams")


@app.before_first_request
def init_db():
    Database.initialize()


@app.route('/')
def home():
    return render_template('home.html')
