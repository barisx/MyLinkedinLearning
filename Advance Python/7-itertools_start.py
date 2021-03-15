# advanced iteration functions in the itertools package

import itertools
from functools import Counter
def testFunction(x):
    return x < 40


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    
    # TODO: use count to create a simple counter
    count1 = itertools.count(100,10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    # Out
    """
        100
        110
        120
        130
    """
    # TODO: accumulate creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    # python3 only
    # acc = itertools.accumulate(vals, max)  
    # print(list(acc))

    # TODO: use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))
    # Out
    """
        ['A', 'B', 'C', 'D', '1', '2', '3', '4']
    """
    
    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))
    
    # Out
    """
        [40, 50, 40, 30]  # drophile
        [10, 20, 30]      # takewhile
    """
if __name__ == "__main__":
    main()