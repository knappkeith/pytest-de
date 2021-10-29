import pytest


@pytest.fixture(name="table_configuration", scope="module")
def fixture_table_configuration():
    return {
        "landing": {
            "db_name": "LT_Landing",
            "table_name": "addr"
        },
        "staging": {
            "db_name": "LT_Staging",
            "table_name": "addr"
        }
    }
