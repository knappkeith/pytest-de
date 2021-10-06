import pytest
from common_tests.TableValidation import TestTableValidation


expected_row_count_data = 1000


@pytest.fixture(name="db_level", scope="module")
def fixture_db_level():
    return "landing"
