#

from bank import value

def main():
    test_return_zer0()



def test_return_zer0():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hello Jashan") == 0


def test_return_20():
    assert value("hii") == 20
    assert value("hlo") == 20


def test_return_100():
    assert value("what?") == 100
    assert value("good morning") == 100

if __name__ == "__main__":
    main()
