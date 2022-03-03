from app.operaciones import cociente


class TestClass:
    def test_cociente(self):
        assert cociente(10, 4) == 2
        assert cociente(100, 9) == 11
        assert cociente(10, 6) == 1
        assert cociente(3, 2) == 1
