from app.operaciones import multiplicacion


class TestClass:
    def test_multiplicacion(self):
        assert multiplicacion(3, 2) == 6
        assert multiplicacion(20, 10) == 200
        assert multiplicacion(10, 5) == 50
        assert multiplicacion(1, 1) == 1
