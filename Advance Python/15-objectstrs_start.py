# customize string representations of objects


class Person():
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25
    
    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self):
        return "<Person Class - fname:{0}, lname:{1}, age:{2}".format(
            self.fname, self.lname, self.age
        )
        
    # TODO: use str for a more human-readable string
    def __str__(self):
        return "Person ({0} {1} is {2})".format(self.fname, self.lname, self.age)
    
    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(
            self.fname, self.lname, self.age
        )
        
        return bytes(val.encode('utf-8'))
        
def main():
    # create a new Person object
    cls1 = Person()
    
    # # use different Python functions to convert it to a string
    # print(repr(cls1))  # <__main__.Person instance at 0x7fbbf2dbdcd0>
    # print(str(cls1))   # <__main__.Person instance at 0x7fbbf2dbdcd0>
    # print("Formatted: {0}".format(cls1))
    # #         Formatted: <__main__.Person instance at 0x7fbbf2dbdcd0>

    
    # use different Python functions to convert it to a string
    print(repr(cls1))  # <Person Class - fname:Joe, lname:Marini, age:25
    print(str(cls1))   # Person (Joe Marini is 25)
    print("Formatted: {0}".format(cls1))  # Formatted: Person (Joe Marini is 25)
    print(bytes(cls1))
    #  Person (Joe Marini is 25)  # Python2
    #  b'Person:Joe:Marini:25'    # Python3
if __name__ == "__main__":
    main()
    