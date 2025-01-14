import pytest
from django.core.management import call_command


def _load_test_fixtures(django_db_blocker):
    """
    Loads all JSON fixtures. Some of these fixtures have to be loaded in order, because they have dependencies on each
    other.
    """
    fixtures = [
        "area-type",
    ]
    with django_db_blocker.unblock():
        for fixture in fixtures:
            print(f"MNEIA-EXPORTER TESTS: Loading fixture {fixture}.json...")
            call_command("loaddata", f"mneia_exporter/tests/fixtures/{fixture}.json")


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    _load_test_fixtures(django_db_blocker)
