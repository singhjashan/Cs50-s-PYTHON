#

from plates import is_valid

def main():
    test_min_max_chr()
    test_strt_with_two()
    test_no_middle()
    test_no_zero()
    test_pun()


def test_min_max_chr():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_strt_with_two():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("22") == False
    assert is_valid("2A") == False

def test_no_middle():
    assert is_valid("AA22") == True
    assert is_valid("AA222A") == False

def test_no_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_pun():
    assert is_valid("PB.46") == False
    assert is_valid("CS!50") == False



if __name__ == "__main__":
    main()
