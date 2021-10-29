import pytest
from helpers.ProtectedString import ProtectedString


@pytest.fixture(name="env_config", scope="session")
def fixture_env_config():
    return {
        "sql": {
            "user": "root",
            "password": ProtectedString("slalomTest"),
            "host": "127.0.0.1",
            "database": "mysql"
        }
    }
