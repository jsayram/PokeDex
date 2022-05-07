#this file will will make the 'website' directory a python package, anything in here will run automatically once website folder is imported
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ramdomcharcter secretkeyydfanadnvsll'

    #importing blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app