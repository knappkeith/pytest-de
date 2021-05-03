import pytest


@pytest.fixture()
def fixture_level_name():
    return "inner_level_fixture_module"


def test_fixture_scope(fixture_scope):
    print(fixture_scope)
    assert False