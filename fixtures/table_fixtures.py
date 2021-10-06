import pytest


@pytest.fixture(name="table_name", scope="module")
def fixture_table_name(table_configuration, db_level):
    table_name = table_configuration[db_level]['table_name']
    print(
        "Retrieving Table Name configuration for "
        f"'{db_level}': '{table_name}'"
    )
    return table_name


@pytest.fixture(name="db_name", scope="module")
def fixture_db_name(table_configuration, db_level):
    db_name = table_configuration[db_level]['db_name']
    print(
        "Retrieving DataBase Name configuration for "
        f"'{db_level}': '{db_name}'"
    )
    return db_name


@pytest.fixture(name="sel_where_clause", scope="module")
def fixture_sel_where_clause():
    return ""


@pytest.fixture(name="sel_select_stmt", scope="module")
def fixture_sel_select_stmt():
    return "*"
