import pytest
import mysql.connector


@pytest.fixture(name="sql_con", scope="session")
def fixture_sql_con(env_config):
    print(f"Connecting to MySQL HOST: {env_config['sql']['host']}")
    return mysql.connector.connect(**env_config["sql"])


@pytest.fixture(name="db_con", scope="module")
def fixture_db_con(sql_con, db_name):
    cursor = sql_con.cursor()
    print(f"Switching DataBase to: '{db_name}'")
    cursor.execute(f"USE {db_name};")
    return sql_con
