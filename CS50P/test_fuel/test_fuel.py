from fuel import gauge,convert
import pytest

def test_ctotal():
    assert convert('99/100') == 99

def test_cvacio():
    assert convert('1/100') == 1

def test_cmedio():
    assert convert('63/100') == 63

def test_gtotal():
    assert gauge(99) == 'F'

def test_gvacio():
    assert gauge(1) == 'E'

def test_gmedio():
    assert gauge(63) == '63%'

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value_error():
    with pytest.raises(ValueError):
        convert('cat/log')
