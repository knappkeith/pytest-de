import pytest
from helpers.query_helpers import run_query


@pytest.fixture(name="sel_sql_str", scope="module")
def fixture_select_sql_str(table_name, sel_select_stmt, sel_where_clause):
    sql = f"""SELECT {sel_select_stmt}
        FROM {table_name}
        {sel_where_clause}
    """
    sql = sql.strip()
    return sql


@pytest.fixture(name="sel_df", scope="module")
def fixture_sel_df(db_con, sel_sql_str):
    return run_query(db_con, sel_sql_str)


@pytest.fixture(scope="module")
def select_df(db_con, table_configuration, db_level):
    sql = f"""SELECT *
        FROM {table_configuration[db_level]['table_name']}
    """
    sql = sql.strip()
    return run_query(db_con, sql)
