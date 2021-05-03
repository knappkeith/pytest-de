def test_simple_assert():
    assert True

class TestBasicClass():
    def test_from_class(_, fixture_scope):
        print(fixture_scope)
        assert False

    def test_from_class_reversed(_, fixture_scope):
        print(fixture_scope[::-1])
        assert False