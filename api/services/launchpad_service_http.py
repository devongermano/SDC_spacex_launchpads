import requests

from api.models import LaunchpadSchema
from api.services import LaunchpadServiceBase


# A class that inherits from our python abstract base class LaunchpadServiceBase,
# we can replace LaunchpadServiceHttp later with something like LaunchpadServiceDB
# in our dependency injector, and everything will be dandy
class LaunchpadServiceHttp(LaunchpadServiceBase):

    def get_launchpads(self):
        # Get launchpad data from the SpaceX API
        launchpad_data = requests.get('https://api.spacexdata.com/v2/launchpads').json()

        # many=true is used to pass collections
        schema = LaunchpadSchema(many=True)

        # Marshmallow handles the validation of the objects we received from SpaceX,
        # verify the data matches the schema and return that as a list our Launchpad class
        result = schema.load(launchpad_data)

        # Return a list of launchpads with the fields from the schema
        return schema.dumps(result)
