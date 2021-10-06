import pandas as pd
from inspect import cleandoc
from textwrap import indent


def run_query(connection, query_string: str) -> pd.DataFrame:
    if "\n" in query_string:
        start_txt = "Running Query : "
        formatted_q = indent(
            cleandoc(query_string), ' ' * len(start_txt)).lstrip()
        print(f"{start_txt}{formatted_q}")
    else:
        print(f"Running Query : {query_string}")
    return pd.read_sql_query(sql=query_string, con=connection)
