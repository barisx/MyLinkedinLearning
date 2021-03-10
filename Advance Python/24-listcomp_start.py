# Demonstrate how to use list comprehensions


def main():
    # define two list of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # TODO: Perform a mapping and filter function on a list
    evenSquared = list(
        map(lambda e: e**2, filter(lambda e: e>4 and e<16, evens)))
    print(evenSquared)


    # TODO: Derive a new list of numbers frm a given list
    evenSquared = [e ** 2 for e in evens]
    print(evenSquared)


    # TODO: Limit the items operated on with a predicate condition
    oddSquared = [e ** 2 for e in odds if e > 3 and e < 17]
    print(evenSquared)
    
    
if __name__ == "__main__":
    main()