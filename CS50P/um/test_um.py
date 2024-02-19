from um import count

def test_coorect():
    assert count('um') == 1

def test_coorect2():
    assert count('um?') == 1

def test_coorect3():
    assert count('Um, thanks for the album.') == 1

def test_coorect4():
    assert count('Um, thanks, um...') == 2