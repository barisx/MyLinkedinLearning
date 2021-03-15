# Demonstrate the usage of defaultdict obejcts

from collections import defaultdict

def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']
    
    # use a dictionary to count each element
    # after adding default dict we commented below line
    fruitCounter = {}
    
    fruitCounter = defaultdict(int)

    """Out
    orange: 1
    grape: 1
    pear: 1
    apple: 2
    banana: 3
    """
    
    # fruitCounter = defaultdict(lambda: 100)
    """Out
    orange: 101
    grape: 101
    pear: 101
    apple: 102
    banana: 103
    """
    
    # Count the elements in the list
    for fruit in fruits:
        fruitCounter[fruit] += 1
        
    # print the result
    # after adding default dict we commented below lines
    for (k, v) in fruitCounter.items():
        if fruit in fruitCounter.keys():
            print(k + ": " + str(v))
    else:
        fruitCounter[fruit] = 1
    # for (k, v) in fruitCounter.items():
    #     print(k + ": " + str(v))
    
if __name__ == "__main__":
    main()