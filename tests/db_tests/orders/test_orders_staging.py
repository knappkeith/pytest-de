import pytest
from common_tests.TableValidation import TestTableValidation


# Configuration for `TestTableValidation.test_expected_row_count`
expected_row_count_data = 0

# Configuration for `TestTableValidation.test_expected_row_type`
expected_row_type_data = [("email", "email")]

# Array of Tests that we expect to fail
xfail_tests = [
    "test_expect_table_not_empty",
    "test_expected_row_type[email|email]"
]


@pytest.fixture(name="db_level", scope="module")
def fixture_db_level():
    return "staging"
