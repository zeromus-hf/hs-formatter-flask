from flask import Flask
import importlib

app = Flask(__name__)

app.config.update({
    'target_script' : importlib.import_module('target_script')
})

from app import views
