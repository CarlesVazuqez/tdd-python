from app.operaciones import resto


class TestClass:
    def test_resto(self):
        assert resto(10, 4) == 2
        assert resto(100, 9) == 1
        assert resto(10, 6) == 4
        assert resto(5, 2) == 1
