import logging

from flask import Blueprint, abort, make_response
from flask.json import jsonify

from api.models import LaunchpadSchema
from api.services import LaunchpadServiceBase

""" A Flask blueprint that contains the views used for launchpad information,
    blueprints are cool, because they provide a way to modularize views in Flask """

launchpad = Blueprint('launchpad', __name__)
logger = logging.getLogger()

""" The view used to get the launchpad data as Array<Launchpad> """
@launchpad.route('/all', methods=['GET'])
def get_launchpads(launchpad_service: LaunchpadServiceBase):
    launchpads = launchpad_service.get_launchpads()
    return LaunchpadSchema(many=True).dumps(launchpads)

""" The view used to get the launchpad data as Array<Launchpad> """
@launchpad.route('/<padid>', methods=['GET'])
def get_launchpad_by_id(launchpad_service: LaunchpadServiceBase, padid):

    parsed_padid = None
    try:
        parsed_padid = int(padid)
    except ValueError as _:
        abort(make_response(jsonify(message="Invalid value given for 'padid'"), 400))

    found_launchpad = launchpad_service.get_launchpad_by_id(parsed_padid)
    return LaunchpadSchema().dumps(found_launchpad)
