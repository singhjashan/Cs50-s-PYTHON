##

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    is_crrt_frmt = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if is_crrt_frmt:
        grp = is_crrt_frmt.groups()
        # return grp

        if int(grp[1]) > 12 or int(grp[5]) > 12 :
            raise ValueError

        # return grp
        tym = nw_frmt(grp[1], grp[2], grp[3])
        tm = nw_frmt(grp[5], grp[6], grp[7])

        return tym + " to " + tm

    else:
        raise ValueError



def nw_frmt(hours ,minutes, am_pm):
    if am_pm == "PM":
        if int(hours) == 12 :
            nw_hr = 12
        else:
            nw_hr = int(hours)+12
    else:
        if int(hours) == 12 :
            nw_hr = 0
        else:
            nw_hr = int(hours)

    if minutes == None :
        nw_min = ':00'
        nw_time = f"{nw_hr:02}" +  nw_min
    else:
        nw_time = f"{nw_hr:02}" +":"+ minutes

    return nw_time





if __name__ == "__main__":
    main()
