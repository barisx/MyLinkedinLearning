def count_to(count):
    """Our iterator implementation"""
    
    # Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]
    
    # Our built-in iterator
    # Creates a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german)
    print(iterator.__doc__)
    # Iterate through our iterable list
    # Extract the German numbers
    # Put them ini a generator called number
    for position, number in iterator:
        #Returns a 'generator' containing number in German
        yield number
        
# Let's test the generator reuturned by our iterator
for num in count_to(3):
    print("{}".format(num))
    
for num in count_to(4):
    print("{}".format(num))