from api.models import Launchpad


def test_launchpad_object():
    launchpad = Launchpad(0, "test", "retired")
    assert launchpad.full_name == "test"
    assert launchpad.padid == 0
    assert launchpad.status == "retired"
