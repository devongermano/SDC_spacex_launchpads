from json import JSONDecodeError

import flask
import requests
from flask import abort, make_response
from flask.json import jsonify
from marshmallow import ValidationError

from api.models import LaunchpadSchema
from api.services import LaunchpadServiceBase

# A class that inherits from our python abstract base class LaunchpadServiceBase,
# we can replace LaunchpadServiceHttp later with something like LaunchpadServiceDB
# in our dependency injector, and everything will be dandy


class LaunchpadServiceHttp(LaunchpadServiceBase):

    def __init__(self, app_config: flask.Config):
        self.app_config = app_config

    def get_launchpads(self):
        # Get launchpad data from the SpaceX API

        endpoint = self.app_config.get("SPACEX_HTTP_ENDPOINT")

        launchpad_data = None
        try:
            launchpad_data = requests.get(endpoint + 'v2/launchpads').json()
        except (requests.exceptions.RequestException, JSONDecodeError) as error:
            print(error)
            abort(make_response(jsonify(message="The SpaceX API returned an unexpected response."), 502))

        # Marshmallow handles the validation of the objects we received from SpaceX,
        # verify the data matches the schema and return that as a list our Launchpad class
        try:
            result = LaunchpadSchema(many=True).load(launchpad_data)
        except ValidationError as error:
            print(error)
            abort(make_response(jsonify(message="The data returned from the SpaceX API was JSON, but it did not "
                                                "conform to the Launchpad Type."), 502))
            return None

        return result
