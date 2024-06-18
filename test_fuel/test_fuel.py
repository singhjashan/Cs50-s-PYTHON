#

from fuel import convert, gauge
import pytest


def main():
    test_corrt_input()
    test_Zero_division()


def test_corrt_input():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"


def test_Zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/monkey")



if __name__ == "__main__":
    main()
