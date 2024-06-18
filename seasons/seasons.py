#

from datetime import date
import re
import sys
import inflect
# from num2words import num2words



p = inflect.engine()


def main():
    brt_date = input("Date of Birth: ")
    try:
        yr, mn, dy = chk_date(brt_date)

        # print(yr, mn, dy)

    except:
        sys.exit("Invalid Date")

    d_o_b = date(int(yr), int(mn), int(dy))
    today_date = date.today()
    # today_date = "2000-01-1"

    # print(today_date)

    n_yr, n_mn, n_dy = chk_date(str(today_date))

    today = date(int(n_yr), int(n_mn), int(n_dy))

    # dif = today_date - d_o_b
    dif = today - d_o_b
    ttl_min = dif.days * 24 * 60

    ans = p.number_to_words(ttl_min, andword="")
    # print(ttl_min)

    print(ans.capitalize() + " minutes")




def chk_date(date):
    if re.search(r"^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}$", date):
        yr, mn, dy = date.split("-")
        return yr, mn, dy





if __name__ == "__main__":
    main()
