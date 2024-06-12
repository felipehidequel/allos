from routes.home import home
from routes.login import login_route
import os
import dotenv

def configure_all(app):
    configure_routes(app)
    configure_x_api()

def configure_routes(app):
    app.register_blueprint(home)
    app.register_blueprint(login_route)

def configure_x_api():
  ...