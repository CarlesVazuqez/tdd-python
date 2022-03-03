from app.operaciones import division


class TestClass:
    def test_division(self):
        assert division(4, 2) == 2
        assert division(20, 10) == 2
        assert division(100, 10) == 10
        assert division(25, 5) == 5
