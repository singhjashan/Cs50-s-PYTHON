#

def main():
    tym = input("what time is it? ")
    time = convert(tym)

    if time >= 7 and time <=8 :
        print("Breakfast time")

    if time >=12 and time<=13 :
        print("Lunch time")

    if time >= 18 and time <= 19 :
        print("Dinner time")


# converting the time
def convert(time):
    hours , minutes = time.split(":")

    new_min = float(minutes)/60
    return float (hours) + new_min



if __name__ == "__main__":
    main()
