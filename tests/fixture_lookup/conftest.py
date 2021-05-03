import pytest


@pytest.fixture()
def fixture_level_name_conftest(fixture_level_name):
    return f"main_level_fixture_conftest - {fixture_level_name}"