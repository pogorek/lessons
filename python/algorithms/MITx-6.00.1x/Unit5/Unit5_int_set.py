class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        """ Returns a new intSet containing elements that appear in both sets """
        new = intSet()
        
        for item in self.vals:
            if item in other.vals:
                new.insert(item)
        return new
    
    def __len__(self):
        """ Returns the number of elements in self """
        return len(self.vals)
        
        
        
# x = intSet()
# y = intSet()
# x.insert(4)
# x.insert(5)
# x.insert(6)
# y.insert(4)
# y.insert(6)
# y.insert(3)

# print(x)
# print(x.intersect(y))
# print(len(x))











