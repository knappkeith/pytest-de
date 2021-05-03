import os
import random
import pytest


@pytest.fixture()
def fixture_level_name():
    return "DEFAULT_level_fixture_module"

@pytest.fixture()
def fixture_level_name_conftest(fixture_level_name):
    return f"DEFAULT_level_fixture_conftest - {fixture_level_name}"


@pytest.fixture()
def fixture_scope(fixture_level_name_conftest):
    yield f"top_level_conftest - {fixture_level_name_conftest}"
    print("I'm back")


@pytest.fixture(scope="session")
def get_token(pytestconfig):
    if pytestconfig.option.token is None:
        return os.getenv("TOKEN")
    return pytestconfig.option.cmdopt


@pytest.fixture(scope="session")
def session_rand_num():
    print("Session Random Number")
    return random.randrange(0, 101, 2)


@pytest.fixture(scope="module")
def module_rand_num():
    print("Module Random Number")
    return random.randrange(0, 101, 2)


@pytest.fixture()
def function_rand_num():
    print("Function Random Number")
    return random.randrange(0, 101, 2)


def pytest_addoption(parser):
    parser.addoption("--token", action="store", default=None,
        help="token for tempest")

