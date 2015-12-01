# Tyler Port

import math


# Problem B.1
class Point(object):
    """
        A set of three values which describe a point in euclidean space
    """
    def __init__(self, x, y, z):
        """

        Args:
            x (float): a x coordinate in euclidean space
            y (float): a y coordinate in euclidean space
            z (float): a z coordinate in euclidean space

        Returns:
            Initializes a Point object.
        """
        self.x = x
        self.y = y
        self.z = z

    def distanceTo(self, endpoint):
        """

        Args:
            endpoint (Point): A valid Point object.

        Returns:
            float: The square root of the sum of the square of the difference
            between this Point's x, y, and z values
        """
        return math.sqrt((self.x - endpoint.x)**2 +
                         (self.y - endpoint.y)**2 +
                         (self.z - endpoint.z)**2)


# Problem B.2
class Triangle(object):
    """


    """
    def __init__(self, vertexA, vertexB, vertexC):
        """

        Args:
            vertexA (Point): a Point object describing the first vertex of
                this triangle.
            vertexB (Point): a Point object describing the second vertex of
                this triangle.
            vertexC (Point): a Point object describing the third vertex of
                this triangle.

        Returns:
            Initializes a valid triangle object.
        """
        self.vertexA = vertexA
        self.vertexB = vertexB
        self.vertexC = vertexC

    def area(self):
        """

        Returns: The area of this triangle formulated using Heron's formula

        """
        a = self.vertexA.distanceTo(self.vertexB)
        b = self.vertexB.distanceTo(self.vertexC)
        c = self.vertexC.distanceTo(self.vertexA)
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area


# Problem B.3
class Averager(object):
    nums = []
    total = 0
    n = 0

    def getNums(self):
        """

        Returns List[numbers]: returns a copy of the current list of numbers.

        """
        return list(self.nums)

    def append(self, number):
        """

        Args:
            number (number): A number to append to the current list of
                numbers.

        Returns:
            Updates the internal state of the object to reflect the
                new list of nums.

        """
        self.nums.append(number)
        self.total += number
        self.n += 1

    def extend(self, number_list):
        """

        Args:
            number_list (List[numbers]): a list of numbers to be appended
                to the stored list of numbers.

        Returns:

        """
        self.nums += number_list
        self.total += sum(number_list)
        self.n += len(number_list)

    def average(self):
        """

        Returns (float): The average of the numbers in the list, or 0.0 if the list is empty

        """
        if self.n != 0:
            return float(self.total) / float(self.n)
        return 0.0

    def limits(self):
        """

        Returns (Tuple[number, number]): Returns a tuple of the minimum and
            maximum of the list of numbers stored, or (0, 0) if the list is
            empty.

        """
        if self.n == 0:
            return 0, 0
        return min(self.nums), max(self.nums)


# Problem C.1
# There's no need for the extra else statement.
def is_positive(x):
    '''Test if x is positive.'''
    return x > 0


# Problem C.2
# No need to define extra variables, or the check if found after the loop.
def find(x, lst):
    '''Returns the index into a list where x is found, or -1 otherwise.
    Assume that x is found at most once in the list.'''
    for i, item in enumerate(lst):
        if item == x:
            return i
    return -1


# Problem C.3
# Should use elif to avoid extra if checks before the functions returns.
def categorize(x):
    '''Return a string categorizing the number 'x', which should be
    an integer.'''
    if x < 0:
        category = 'negative'
    elif x == 0:
        category = 'zero'
    elif x > 0 and x < 10:
        category = 'small'
    elif x >= 10:
        category = 'large'
    return category


# Problem C.4
# Function to do this already exists in the standard library.
def sum_list(lst):
    '''Returns the sum of the elements of a list of numbers.'''
    final_value = 0
    for number in lst:
        final_value += number
    return final_value

