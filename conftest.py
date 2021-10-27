import pytest

pytest.register_assert_rewrite("common_tests")

from typing import Any, Callable, Optional

from _pytest.python import Module

from common_tests.TableValidation import TestTableValidation
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


def generate_params_ids_parametrized_list(
        data_name: str,
        module: Module,
        ids_func: Callable,
        data_default: Optional[Any] = None,
        data_compare: Optional[Callable] = None) -> dict:
    """Builds the `params` and `ids` for generated parametrized tests."""

    # Set Defaults
    if data_default is None:
        data_default_value = []
    else:
        data_default_value = data_default
    if data_compare is None:
        def data_compare_func(x):
            return len(x) > 0
    else:
        data_compare_func = data_compare

    # Get the required values from the module
    module_data = get_dependant_module_attribute(
        module,
        data_name,
        data_default_value)

    # Determine if data present
    if data_compare_func(module_data):
        ids = ids_func

        # The `argvalues` parameter for parametrize requires an iterable
        if hasattr(module_data, "__iter__"):
            params = module_data
        else:
            params = [module_data]
    else:

        # This is the skip logic
        ids = ["Not Configured"]
        params = [pytest.param(
            [],
            marks=pytest.mark.skip(
                reason=f"No Configured `{data_name}` values"))]
    return {"argvalues": params, "ids": ids}
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
    gen_test_name = "expected_row_count"
    if f"{gen_test_name}_value" in metafunc.fixturenames:
        mark_info = generate_params_ids_parametrized_list(
            data_name=f"{gen_test_name}_data",
            module=metafunc.module,
            ids_func=None,
            data_default=-1,
            data_compare=lambda x: x > -1)
        metafunc.parametrize(f"{gen_test_name}_value", **mark_info)

    # Parametrize for `test_expected_row_type`
    gen_test_name = "expected_row_type"
    if f"{gen_test_name}_value" in metafunc.fixturenames:
        mark_info = generate_params_ids_parametrized_list(
            data_name=f"{gen_test_name}_data",
            module=metafunc.module,
            ids_func=TestTableValidation.expected_row_type_value_ids)
        metafunc.parametrize(f"{gen_test_name}_value", **mark_info)
###############################################################################
