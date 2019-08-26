from flask import Flask
from flask_injector import FlaskInjector, request

from api.blueprints.launchpad import launchpad
from api.services import LaunchpadServiceHttp, LaunchpadServiceBase

app = Flask(__name__)

app.register_blueprint(launchpad, url_prefix='/api/launchpads')


@app.after_request
def apply_caching(response):
    response.headers["Content-type"] = "application/json"
    return response


def configure(binder):
    binder.bind(
        LaunchpadServiceBase,
        to=LaunchpadServiceHttp(),
        scope=request,
    )


# if __name__ == '__main__':
FlaskInjector(app=app, modules=[configure])
# app.run(debug=True)
