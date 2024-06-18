#

from seasons import chk_date

def main():
    test_chk_bdy()


def test_chk_bdy():
    assert chk_date("2004-09-20") == ("2004","09","20")
    assert chk_date("2004-9-20") == ("2004","9","20")
    assert chk_date("september 20, 2004") == None


if __name__ == "__main__":
    main()
