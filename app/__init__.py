from flask import Flask
from config import Config

print('Printing name: {}'.format(__name__))
app = Flask(__name__)
app.config.from_object(Config)

from app import routes
