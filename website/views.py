#the url endpoints for the functioning url on the website, home page etc...
from flask import Blueprint, render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')
    