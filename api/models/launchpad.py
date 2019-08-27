from marshmallow import Schema, fields, EXCLUDE, post_load


class Launchpad(object):
    def __init__(self, padid: int, full_name: str, status: str):
        self.padid = padid
        self.full_name = full_name
        self.status = status


class LaunchpadSchema(Schema):
    """A marshmallow representation of what we expect our data to be like,
    this also gives us cool things like deserialization and serialization from JSON"""

    """ Ignore unknown fields from the SpaceX API, otherwise unexpected parameters in the
    JSON would cause Marshmallow to throw runtime errors """
    class Meta:
        unknown = EXCLUDE

    padid = fields.Integer()
    full_name = fields.String()
    status = fields.String()

    """ This decorated method is used by marshmallow for deserialization into our Launchpad class """
    @post_load
    def make_user(self, data, **kwargs):
        return Launchpad(**data)
