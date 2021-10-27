import pytest
from common_tests.TableValidation import TestTableValidation


expected_row_count_data = 499

expected_row_type_data = [("email", "email"), ("ip_address", "ip")]


@pytest.fixture(name="db_level", scope="module")
def fixture_db_level():
    return "staging"
