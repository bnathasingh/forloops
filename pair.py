"""
The class definition for Lab 8

The class Pair should have exactly two methods in it: __init__ and sum.  The __init__
method should initialize the first and second attributes.  The sum method returns the
sum of these two attributes.

Initial skeleton by W. White (wmw2)

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


class Pair(object):
    """
    A class representing a pair of values.

    Attribute first: The first value
    Invariant: first is an int

    Attribute second: The second value
    Invariant: second is an int

    This class has a single method: sum(). This method returns
    the sum of first and second.
    """
    def __init__(self, x, y):
        self.first= x
        self.second = y
    def sum(object):
        sum = object.first + object.second
        return sum

    pass # Implement me
