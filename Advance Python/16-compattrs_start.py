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
        super().__setattr__(attr, val)  # Python3 style
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

        
    # TODO: use dir to list the available properties
    def __dir__(self):
        return ("red", "green", "blue", "rgbcolor", "hexcolor")

def main():
    # create an instance fof myColor
    cls1 = myColor()
    
    # TODO: print the value if a computed attribute
    print(cls1.rgbcolor)  # (50, 75, 100)
    print(cls1.hexcolor)  # #{0:02x}{1:02x}{2:02x}
    
    # TODO: set the value of a computed attribute
    cls1.rbgcolor = (125, 200, 86)
    print(cls1.rbgcolor)  # (125, 200, 86)
    print(cls1.hexcolor)  # #{0:02x}{1:02x}{2:02x}
    
    # TODO: access a regular attribute
    print(cls1.red)
    # 50
    
    # TODO: list the available attributes
    print(dir(cls1))
    # ['blue', 'green', 'hexcolor', 'red', 'rgbcolor']
    
if __name__ == "__main__":
    main()