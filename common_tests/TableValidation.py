import numpy as np
import pandas as pd


class TestTableValidation():
    @staticmethod
    def expected_row_type_value_ids(item: tuple) -> str:
        return f"{item[0]}|{item[1]}"

    def test_expected_row_count(_, sel_df, expected_row_count_value):
        assert len(sel_df.index) == expected_row_count_value

    def test_expected_row_type(_, sel_df, expected_row_type_value):
        column_name = expected_row_type_value[0]
        value_type = expected_row_type_value[1]

        if value_type == "email":
            def comp_func(x):
                return len(x.split("@")) == 2 and \
                    len(x.split("@")[1].split(".")) >= 2
        elif value_type == "ip":
            def comp_func(x):
                return len(x.split(".")) == 4
        comp_df = sel_df[sel_df[column_name].apply(comp_func)]
        assert len(comp_df.index) == len(sel_df.index)

    def demo(_):
        assert False
