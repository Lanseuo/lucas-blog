import os

from flask import Flask
from flask_cors import CORS
from pathlib import Path

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

top_level_path = Path(os.path.realpath(__file__)).parent.parent

from .routes import *  # noqa
