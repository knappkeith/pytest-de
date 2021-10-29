import pytest


# pytestmark for entire file
pytestmark = pytest.mark.landing


@pytest.fixture(name="db_level", scope="module")
def fixture_db_level():
    return "landing"


def test_expect_table_not_empty(select_df):
    """Test to ensure there is at least one record in the Table"""
    assert len(select_df.index) > 0


@pytest.mark.smoke
def test_expect_table_to_have_user_id_column(select_df):
    """Test to ensure that the table has the column named 'user_id'"""
    assert "user_id" in select_df.columns
