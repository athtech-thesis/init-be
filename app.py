import os 
from flask import Flask, url_for, jsonify
import controllers
from flask_cors import CORS
from db.db import db
from dotenv import load_dotenv
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)


if os.getenv("ENV") == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.secret_key = str(os.getenv("SECRET_ΚΕΥ"))

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.secret_key = str(os.getenv("SECRET_ΚΕΥ"))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# PING ENDPOINTS
app.register_blueprint(controllers.ping_controller.api) 
# AUTHORIZATION ENDPOINTS
app.register_blueprint(controllers.authorization_controller.api)
#  USER ENDPOINTS
app.register_blueprint(controllers.user_controller.api)

db.init_app(app)
migrate = Migrate(app, db)

CORS(app)

if __name__ == '__main__':
    app.run(port=3000)

