from seasons import calculate_minuts
import pytest

def test_fecha_ok():
    assert calculate_minuts('2020-10-11') == ('One million, fifty-one thousand, two hundred minutes')


def test_fecha_nook():
    with pytest.raises(SystemExit):
        calculate_minuts('january , 2 1988')

