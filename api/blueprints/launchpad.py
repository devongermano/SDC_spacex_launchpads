from flask import Blueprint, jsonify, Response
from api.services import LaunchpadServiceBase
# A Flask blueprint that contains the views used for launchpad information,
# blueprints are cool, because they provide a way to modularize views in Flask

launchpad = Blueprint('launchpad', __name__)


# The view used to get the launchpad data as Array<Launchpad>
@launchpad.route('/', methods=['GET'])
def get_launchpads(launchpad_service: LaunchpadServiceBase):
    launchpads = launchpad_service.get_launchpads()
    return launchpads
