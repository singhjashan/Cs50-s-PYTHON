#

from um import count

def main():
    test_lwr_cse()
    test_wrd_wth_um()
    test_srrnd_spce()


def test_lwr_cse():
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2



def test_wrd_wth_um():
    assert count("yummi") == 0



def test_srrnd_spce():
    assert count("hello, um world ") == 1
    assert count(" um ") == 1





if __name__ == "__main__":
    main()
