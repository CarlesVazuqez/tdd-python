from app.operaciones import resta


class TestClass:
    def test_resta(self):
        assert resta(3, 2) == 1
        assert resta(20, 10) == 10
        assert resta(13, 5) == 8
        assert resta(5, 5) == 0
