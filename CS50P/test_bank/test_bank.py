from bank import value

def test_hello():
    assert value('hello sir') == 0
    assert value('HELLOWORLD') == 0

def test_h():
    assert value('hi Diego') == 20
    assert value('HISIR') == 20

def test_other():
    assert value('SUPER HELLO') == 100
    assert value('not hi') == 100




