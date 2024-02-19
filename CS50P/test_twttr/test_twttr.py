from twttr import shorten

def test_vocales():
    assert shorten('hola') == 'hl'

def test_numbers():
    assert shorten('hola 2') == 'hl 2'

def test_puntuacion():
    assert shorten('world ...') == 'wrld ...'

def test_mayuscula():
    assert shorten('CAT') == 'CT'