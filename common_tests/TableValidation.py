def test_simple_assert():
    assert True


class TestTableValidation():

    def test_expected_row_count(_, sel_df, expected_row_count_value):
        assert len(sel_df.index) == expected_row_count_value
