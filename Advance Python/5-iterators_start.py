# use iterator functions like enumerate, zip, iter, next



def main():
    # define a list of days iin English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    # i = iter(days)
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))
    """Out
    Sun
    Mon
    Tue
    Wed
    """
    # TODO: iterate using a function and sentinel 
    # with open("5-testfile.txt", "r") as fp:
    #     for line in iter(fp.readline, ''):
    #         print(line)
    """Out
    This is line 1

    This is line 2

    This is line 3

    This is line 4

    This is line 5

    This is line 6
    """
    # TODO: use regular iteration over the days
    for m in days:
        print(m)
    """Out
    Sun
    Mon
    Tue
    Wed
    Thu
    Fri
    Sat
    """
    
    # for m in range(len(days)):
    #     print(m+1, days[m])


    
    # TODO: using enumerate reduces code and provides a counter
    # for i, m in enumerate(daysm start=1):
    #     print(i, m)

    # TODO: use zip to combine sequences
    # for m in zip(days, daysFR):
    #     print(m)
    
    # for i, m in enumerate(zip(days, daysFR), start=1):
    #     print(i, m[0], "=", m[1], "in French")

if __name__ == "__main__":
    main()