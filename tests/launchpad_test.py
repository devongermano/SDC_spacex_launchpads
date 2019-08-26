from api.models import Launchpad, LaunchpadSchema
from api.services import LaunchpadServiceHttp


def test_launchpad_object():
    launchpad = Launchpad(0, "test", "retired")
    assert launchpad.full_name == "test"
    assert launchpad.padid == 0
    assert launchpad.status == "retired"


def test_launchpad_service_http():
    launchpad_service_http = LaunchpadServiceHttp()
    # Ensure the SpaceX is actually returning data
    assert len(launchpad_service_http.get_launchpads()) > 0

    # Check if the dict returned by the LaunchpadSchema is the same dict as Launchpad
    schema = LaunchpadSchema(many=True)
    launchpads = schema.loads(launchpad_service_http.get_launchpads())
    assert isinstance(Launchpad(0, "test", "retired"), type(launchpads[0]))
