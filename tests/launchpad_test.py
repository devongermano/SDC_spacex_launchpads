import pytest

from api.models import Launchpad, LaunchpadSchema


@pytest.fixture
def launchpad():
    launchpad = Launchpad(0, "test", "retired")
    return launchpad


def test_launchpad_object():
    launchpad = Launchpad(0, "test", "retired")
    assert launchpad.full_name == "test"
    assert launchpad.padid == 0
    assert launchpad.status == "retired"
    return launchpad


# Verify that the schema returns the correct type of object (Launchpad)
def test_launchpad_marshmallow_schema(launchpad):
    test_launchpad_json_data = '{"full_name": "Test Complex", "status": "retired", "padid": -1}'
    data = LaunchpadSchema().loads(test_launchpad_json_data)
    assert isinstance(data, type(launchpad))
