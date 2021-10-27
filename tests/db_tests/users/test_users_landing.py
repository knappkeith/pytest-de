import pytest
from common_tests.TableValidation import TestTableValidation
from helpers.query_helpers import run_query


expected_row_count_data = 999
expected_row_type_data = [("email", "email"), ("ip_address", "ip")]


@pytest.fixture(name="db_level", scope="module")
def fixture_db_level():
    return "landing"


def test_ensure_table_not_empty(select_df):
    assert len(select_df.index) > 0
