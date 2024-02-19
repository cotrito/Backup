from jar import Jar

def size():
    jar = Jar()
    return jar.size

def create():
    jar = Jar(10)
    return jar.capacity

def deposit():
    jar = Jar()
    jar.deposit(10)
    return jar.size

def withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(2)
    return jar.size

def test_size():
    assert size() == 0

def test_create():
    assert create() == 10

def test_deposit():
    assert deposit() == 10

def test_with():
    assert withdraw() == 8



