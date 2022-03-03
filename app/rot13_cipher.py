def rot13_cipher(phrase):
    """Funcion para hacer cifrado rot13"""
    abc = "abcdefghijklmnopqrstuvwxyz"
    cifrado = ""
    for char in phrase:
        cifrado += abc[(abc.find(char)+13) % 26]
    return cifrado
