import pytest
from common_tests.TableValidation import TestTableValidation


# Configuration for `TestTableValidation.test_expected_row_count`
expected_row_count_data = 500

# Configuration for `TestTableValidation.test_expected_row_type`
expected_row_type_data = []


@pytest.fixture(name="db_level", scope="module")
def fixture_db_level():
    return "staging"
