# define enumerations using the Enum base class

from enum import Enum, unique, auto


# class Fruit(Enum):
#     APPLE = 1
#     BANANA = 2
#     ORANGE = 3
#     TOMATO = 4
#     RED_DELICIOUS = 1  # still work
    
# @unique
# class Fruit(Enum):
#     APPLE = 1
#     BANANA = 2
#     ORANGE = 3
#     TOMATO = 4
#     RED_DELICIOUS = 1  # ValueError: duplicate names found in <enum 'Fruit'>: APPLE -> RED_DELICIOUS
    
@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()  # Python3 Only
    
def main():
    pass
    # TODO: enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))
    
    """Out
    Fruit.APPLE
    <enum 'Fruit'>
    <Fruit.APPLE: 1>
    """
    
    # TODO: enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)
    # ('APPLE', 1)
    
    # TODO: print the auto-generated value
    print(Fruit.PEAR.value)
    # 5
    # TODO: enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits[Fruit.BANANA])
    # Come Mr. Tally-man
if __name__ == "__main__":
    main()