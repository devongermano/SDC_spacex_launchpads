from flask import Flask
from flask_injector import FlaskInjector, request

from api.blueprints.launchpad import launchpad
from api.services import LaunchpadServiceHttp, LaunchpadServiceBase
from api.util import CustomResponse


# Setup services as modules for injection
def configure(binder):
    binder.bind(LaunchpadServiceBase,
                to=LaunchpadServiceHttp(app.config),
                scope=request)


# Init flask, takes module name as constructor parameter
app = Flask(__name__)

# Grab the values from the config file and add them to app.config
app.config.from_pyfile("config/config.py")

# Force response type as application/json for the entire application
app.response_class = CustomResponse

# Get the launchpad blueprint
app.register_blueprint(launchpad, url_prefix='/api/launchpad')

# Inject services
FlaskInjector(app=app, modules=[configure])
