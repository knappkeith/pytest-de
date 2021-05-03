import pytest
import pandas as pd


@pytest.fixture()
def legacy_df():
    return pd.DataFrame(
        {
            "A": [1,2,3],
            "B": ["1", "1", "1"]
        }
    )

@pytest.fixture()
def remediated_df():
    return pd.DataFrame(
        {
            "A": [1,2,3],
            "B": ["1", "1", "1"]
        }
    )


@pytest.mark.parametrize("passed_value", [1, 2, "A"])
def test_passed_value(passed_value):
    print(f"My passed value is: {passed_value}")
    assert isinstance(passed_value, int)


def test_compare_column_names(legacy_df, remediated_df):
    assert sorted(set(remediated_df.columns)) == \
        sorted(set(legacy_df.columns))