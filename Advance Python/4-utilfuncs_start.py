# demonstrate built-in utility functions


def main():
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]

    # TODO: any will return true if any of the sequence values are true
    print(any(list1))
    
    # TODO: all will return true only if all values are true
    print(all(list1))

    """
    def any(iterable):
        for i in iterable:
            if i:
                return True
        return False # for an empty iterable, any returns False!

    def all(iterable):
        for i in iterable:
            if not i:
                return False
        return True  # for an empty iterable, all returns True!
    
    
    +-----------------------------------------+---------+---------+
    |                                         |   any   |   all   |
    +-----------------------------------------+---------+---------+
    | All Truthy values                       |  True   |  True   |
    +-----------------------------------------+---------+---------+
    | All Falsy values                        |  False  |  False  |
    +-----------------------------------------+---------+---------+
    | One Truthy value (all others are Falsy) |  True   |  False  |  # [1, 0, 0, 0, 0, 0, False]
    +-----------------------------------------+---------+---------+
    | One Falsy value (all others are Truthy) |  True   |  False  |  # [1, 2, 3, "", 5, 6, True]
    +-----------------------------------------+---------+---------+
    | Empty Iterable                          |  False  |  True   |
    +-----------------------------------------+---------+---------+
    | Work Style                              |     or  |  and    |
    +-----------------------------------------+---------+---------+
    """
    # TODO: min and max vwill return minimum and maximum values in a sequence
    print("min:", min(list1))
    print("max:", max(list1))
    
    

    # TODO: Use sum() to sum up all of the values in a sequence
    print("sum:", sum(list1))

if __name__ == "__main__":
    main()