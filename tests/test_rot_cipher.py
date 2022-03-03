from app.rot13_cipher import rot13_cipher


class TestClass:
    def test_rot13_cipher(test):
        assert rot13_cipher("hello friend") == "uryyb sevraq"
        assert rot13_cipher("hola amigo") == "ubyn nzvtb"
        assert rot13_cipher("prueba de rot13") == "cehron qr ebg13"
