# customize string representations of objects


class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100
        
    # TODO: use getattr to dynamiccaly return a value
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}"
        else:
            raise AttributeError
            
    
    # TODO:  use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        super().__setattr__(attr, val)
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

        
    # TODO: use dir to list the available properties
    def __dir__(self):
        pass

def main():
    # create an instance fof myColor
    cls1 = myColor()
    
    # TODO: print the value if a computed attribute
    print(cls1.rgbcolor)
    print(cls1.hexcolor)
    
if __name__ == "__main__":
    main()