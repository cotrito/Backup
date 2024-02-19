from plates import is_valid

def test_total():
    assert is_valid('cs50.') == False
    assert is_valid('cs50') == True

def test_largo():
    assert is_valid('cscscs50') == False
    assert is_valid('cscs50') == True

def test_numero():
    assert is_valid('cs50c') == False

def test_comienza0():
    assert is_valid('cs05') == False

def test_comienzaalfa():
    assert is_valid('5050') == False
    assert is_valid('roro') == True