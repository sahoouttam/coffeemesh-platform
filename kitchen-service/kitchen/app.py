from flask import Flask
from flask_smorest import Api

from ch02.kitchen.config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)

kitchen_api = Api(app)
