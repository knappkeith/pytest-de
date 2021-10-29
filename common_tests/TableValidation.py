import pytest


class TestTableValidation():
    @staticmethod
    def expected_row_type_value_ids(item: tuple) -> str:
        """Static Method to determine Parameterization ID for
        `test_expected_row_type`
        """
        return f"{item[0]}|{item[1]}"

    def test_expect_table_not_empty(_, select_df):
        """Test to ensure there is at least one record in the Table"""
        assert len(select_df.index) > 0

    @pytest.mark.smoke
    def test_expected_row_count(_, select_df, expected_row_count_value):
        """Test to ensure that there are a specific number of rows in a table
        """
        assert len(select_df.index) == expected_row_count_value

    def test_expected_row_type(_, select_df, expected_row_type_value):
        """Test to ensure that a specific column has a specific complex data
        type:
            email -> string@string.string
            ip    -> string.string.string.string
        """

        # ensure data in table
        assert len(select_df.index) > 0

        column_name = expected_row_type_value[0]
        value_type = expected_row_type_value[1]

        if value_type == "email":
            def comp_func(x):
                return len(x.split("@")) == 2 and \
                    len(x.split("@")[1].split(".")) >= 2
        elif value_type == "ip":
            def comp_func(x):
                return len(x.split(".")) == 4
        comp_df = select_df[select_df[column_name].apply(comp_func)]
        assert len(comp_df.index) == len(select_df.index)


class TestTableValidationReferentialCheck(TestTableValidation):

    @pytest.mark.skip(reason="This test is still being developed")
    def test_referential_integrity_check(_, select_df):
        """Future Test to ensure Referential Integrity Check"""
        assert True
