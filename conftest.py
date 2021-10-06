import pytest

pytest.register_assert_rewrite("common_tests")

from typing import Any, Optional

from _pytest.python import Module

from fixtures.common_fixtures import fixture_env_config
from fixtures.connection_fixtures import fixture_db_con, fixture_sql_con
from fixtures.select_fixtures import fixture_sel_df, fixture_select_sql_str
from fixtures.table_fixtures import (fixture_db_name, fixture_sel_select_stmt,
                                     fixture_sel_where_clause,
                                     fixture_table_name)


###############################################################################
# Functions
###############################################################################
def get_dependant_module_attribute(
        module: Module,
        attr_name: str,
        default: Optional[Any] = None) -> Any:
    """Returns the attribute requested if it existed in the module."""
    rtn_attr = default
    if hasattr(module, attr_name):
        rtn_attr = getattr(module, attr_name)
    return rtn_attr
###############################################################################


###############################################################################
# Hooks
###############################################################################
# Initialization hooks
def pytest_addoption(parser):
    parser.addoption("--token", action="store", default=None,
                     help="token for tempest")
###############################################################################


###############################################################################
# Python test function related Hooks
def pytest_generate_tests(metafunc):
    """Generate (multiple) parametrized calls to a test function."""

    # Parametrize for `test_expected_row_count`
    if "expected_row_count_value" in metafunc.fixturenames:

        # Get the required values from the module
        expected_value = get_dependant_module_attribute(
            metafunc.module,
            "expected_row_count_data",
            0)

        metafunc.parametrize(
            "expected_row_count_value",
            [expected_value])
###############################################################################
