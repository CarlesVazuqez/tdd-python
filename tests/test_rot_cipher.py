from app.rot13_cipher import rot13_cipher


class TestClass:
    def test_rot13_cipher(test):
        assert rot13_cipher("hellofriend") == "uryybsevraq"
        assert rot13_cipher("holaamigo") == "ubynnzvtb"
        assert rot13_cipher("pruebaderot") == "cehronqrebg"
