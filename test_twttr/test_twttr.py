#

# from twttr import shorten
import twttr

def main():
    test_uppr_or_lowr()
    test_numbers()
    test_punctuations()



def test_uppr_or_lowr():
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("TWITTER") == "TWTTR"
    assert twttr.shorten("TwItTeR") == "TwtTR"



def test_numbers():
    assert twttr.shorten("1234") == "1234"


def test_punctuations():
    assert twttr.shorten("?!,") == "?!,"


if __name__ == "__main__":
    main()
