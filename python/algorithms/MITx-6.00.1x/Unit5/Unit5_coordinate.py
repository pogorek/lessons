class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __repr__(self):
        # Method that returns a string that looks like a valid Python expression that could be used to recreate an object with the same value
        return 'Coordinate({},{})'.format(self.x, self.y)

    def __eq__(self, other):
        # Method that returns True if coordinates refer to same point
        x_bool = self.x == other.x
        y_bool = self.y == other.y
        return x_bool and y_bool
