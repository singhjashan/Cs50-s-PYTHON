#

from working import convert, nw_frmt
import pytest


def main():
    test_wrg_frmt()
    test_tym()
    test_worng_hr()
    test_wrong_min()


def test_wrg_frmt():
    with pytest.raises(ValueError):
        convert('9 AM - 9 PM')


def test_tym():
    assert convert('9 AM to 5 PM') == "09:00 to 17:00"
    assert convert('10 PM to 8 AM') == "22:00 to 08:00"
    assert convert('10:30 AM to 8:50 PM') == "10:30 to 20:50"


def test_worng_hr():
    with pytest.raises(ValueError):
        convert('13 AM to 17 PM')



def test_wrong_min():
    with pytest.raises(ValueError):
        convert('9:60 AM to 9:60 PM')





if __name__ == "__main__":
    main()
