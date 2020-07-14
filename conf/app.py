from flask import Flask
from conf.database import init_db
import conf.models

def create_app():
    app = Flask(__name__)
    app.config.from_object('conf.config.Config')

    init_db(app)

    return app

app = create_app()