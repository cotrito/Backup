from numb3rs import validate

def test_correct1():
    assert validate('1.1.1.1') == True
def test_correct2():
    assert validate('1.10.100.0') == True
def test_correct3():
    assert validate('255.255.255.255') == True

def test_incorrect1():
    assert validate('1.1') == False
def test_incorrect2():
    assert validate('275.3.6.28') == False
def test_incorrect3():
    assert validate('1.1.1.1.1') == False
def test_incorrect3():
    assert validate('1.1.1.300') == False
def test_incorrect4():
    assert validate('1...1') == False