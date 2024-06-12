from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

home = Blueprint('home', __name__)

@home.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        return 'Template not found', 404