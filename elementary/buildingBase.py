'''
The singularity has happened and we are being made to build the ideal robo-city for our overlords. 
In this shining robotropolis, all buildings will be rectangular and all streets laid along south-north and east-west lines 
in a glorious grid. Before we get started, we to create a class to represent the perfect building.

Because all the buildings in the city are rectangular and their walls are parallel to the streets, 
we can define any building using only the coordinates of South-Western corner as two arguments 
(the length of the west to east walls, and the length of the north to south wall) along with the height of the building. 
These values are described as positive numbers using conventional units. 
The origin point of our coordinate system lies in the South-West, 
as a result the northern corner ends up having the greater coordinate value than the southern corner. 
To complete this mission we need to use a couple operations.

In this mission all data will be correct and you don't need to implement value checking.

Input: Statements and expression with the Building class.
Output: The behaviour as described.

How it is used: Here you will learn how to write a simple class with minimal functionality to achieve greater glory for Robonia.
Precondition: All data are correct.
'''

class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        # Returns a new Building instance with the South-West corner at [south, west] coordinates, the size is width_WE by width_NS 
        # and the height of the building is height. "height" is a positive number with a default value of 10.
        self.__s = south
        self.__w = west
        self.__wwe = width_WE
        self.__wns = width_NS
        self.__h = height
        self.__c = {}       # corners

    def corners(self): # returns a dictionary with the coordinates of the building corners
        # The dictionary has following keys: "north-west", "north-east", "south-west", "south-east". 
        # The values are lists or tuples with two numbers.
        self.__c ["north-west"] = [self.__s + self.__wns, self.__w]
        self.__c ["north-east"] = [self.__s + self.__wns, self.__w + self.__wwe]
        self.__c ["south-west"] = [self.__s, self.__w]
        self.__c ["south-east"] = [self.__s, self.__w + self.__wwe]
        return self.__c

    def area(self):     # returns the area of the building
        return self.__wwe * self.__wns

    def volume(self):   # returns the volume of the building
        return self.__wwe * self.__wns * self.__h

    def __repr__(self):
        # This is a string representation of the Building. This method is used for "print" or "str" conversion. 
        # Returns the string in the following view: "Building({south}, {west}, {width_we}, {width_ns}, {height})"
        return "Building(%s, %s, %s, %s, %s)" % (self.__s, self.__w, self.__wwe, self.__wns, self.__h) # or %r, not %d or %f 

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"    
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"