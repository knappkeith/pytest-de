import pytest

pytest.register_assert_rewrite("common_tests")

from typing import List

from _pytest.config import Config
from _pytest.python import Metafunc

from common_tests.TableValidation import TestTableValidation
from fixtures.common_fixtures import fixture_env_config
from fixtures.connection_fixtures import fixture_db_con, fixture_sql_con
from fixtures.select_fixtures import fixture_sel_df, fixture_select_sql_str
from fixtures.table_fixtures import (fixture_db_name, fixture_sel_select_stmt,
                                     fixture_sel_where_clause,
                                     fixture_table_name)
from helpers.query_helpers import run_query


###############################################################################
# Hooks
###############################################################################
# Initialization hooks
def pytest_configure(config) -> None:
    """Allow plugins and conftest files to perform initial configuration.

    This hook is called for every plugin and initial conftest file
    after command line options have been parsed.

    After that, the hook is called for other conftest files as they are
    imported.

    .. note::
        This hook is incompatible with ``hookwrapper=True``.

    :param _pytest.config.Config config: The pytest config object.
    """
    # Add Custom markers
    config.addinivalue_line(
        "markers", "smoke: mark tests for quick validation")
    config.addinivalue_line(
        "markers", "landing: mark tests for landing zone tests")


###############################################################################
# Collection Hooks
def pytest_collection_modifyitems(
        session: pytest.Session,
        config: Config,
        items: List[pytest.Item]):
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param pytest.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
    for item in items:
        if hasattr(item.module, "xfail_tests"):
            xfail_array = getattr(item.module, "xfail_tests")
            if item.name in xfail_array:
                item.add_marker(pytest.mark.xfail(
                    reason="This test is Expected to fail", strict=True))


###############################################################################
# Python test function related Hooks
def pytest_generate_tests(metafunc: Metafunc):
    """Generate (multiple) parametrized calls to a test function."""

    # Parametrize for `test_expected_row_count`
    if "expected_row_count_value" in metafunc.fixturenames:

        # Parametrize fixture if there is data to test, otherwise skip
        if hasattr(metafunc.module, "expected_row_count_data"):
            config_data = getattr(metafunc.module, "expected_row_count_data")
            metafunc.parametrize(
                "expected_row_count_value",
                [config_data])

        else:
            metafunc.parametrize(
                "expected_row_count_value",
                [pytest.param(
                    [],
                    marks=pytest.mark.skip(
                        reason="No Configured `expected_row_count_data` values"
                    ))],
                ids=["Not Configured"]
            )

    # Parametrize for `test_expected_row_type`
    if "expected_row_type_value" in metafunc.fixturenames:

        # Get the value of the data from the module
        if hasattr(metafunc.module, "expected_row_type_data"):
            config_data = getattr(metafunc.module, "expected_row_type_data")
        else:
            config_data = []

        # Parametrize fixture if there is data to test, otherwise skip
        if len(config_data) > 0:
            metafunc.parametrize(
                "expected_row_type_value",
                config_data,
                ids=TestTableValidation.expected_row_type_value_ids)

        else:
            metafunc.parametrize(
                "expected_row_type_value",
                [pytest.param(
                    [],
                    marks=pytest.mark.skip(
                        reason="No Configured `expected_row_type_data` values"
                    ))],
                ids=["Not Configured"]
            )
###############################################################################


###############################################################################
# FIXTURES
###############################################################################
@pytest.fixture(scope="module")
def select_df(db_con, db_level, table_configuration):
    sql = f"""SELECT *
        FROM {table_configuration[db_level]['table_name']}
    """
    sql = sql.strip()
    return run_query(db_con, sql)
###############################################################################
