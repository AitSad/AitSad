import math

class Vector:
    """
    A class to represent a vector in n-dimensional space.

    Attributes:
        coordinates (list): A list of floats representing the coordinates of the vector.

    Methods:
        __init__(self, coordinates)
            Initializes a new instance of the Vector class.
        __str__(self)
            Returns a string representation of the vector.
        __eq__(self, other)
            Determines whether two vectors are equal.
        __add__(self, other)
            Adds two vectors together.
        __sub__(self, other)
            Subtracts one vector from another.
        dot(self, other)
            Computes the dot product of two vectors.
        cross(self, other)
            Computes the cross product of two vectors.
        magnitude(self)
            Computes the magnitude (length) of the vector.
        normalize(self)
            Normalizes the vector (i.e., converts it to a unit vector).

    """

    def __init__(self, coordinates):
        """
        Initializes a new instance of the Vector class.

        Args:
            coordinates (list): A list of floats representing the coordinates of the vector.

        Returns:
            None.

        """
        self.coordinates = coordinates

    def __str__(self):
        """
        Returns a string representation of the vector.

        Args:
            None.

        Returns:
            str: A string representation of the vector.

        """
        return f"Vector: {self.coordinates}"

    def __eq__(self, other):
        """
        Determines whether two vectors are equal.

        Args:
            other (Vector): The other vector to compare with.

        Returns:
            bool: True if the vectors are equal, False otherwise.

        """
        return self.coordinates == other.coordinates

    def __add__(self, other):
        """
        Adds two vectors together.

        Args:
            other (Vector): The vector to add.

        Returns:
            Vector: A new vector representing the sum of the two vectors.

        """
        return Vector([x+y for x,y in zip(self.coordinates, other.coordinates)])

    def __sub__(self, other):
        """
        Subtracts one vector from another.

        Args:
            other (Vector): The vector to subtract.

        Returns:
            Vector: A new vector representing the difference of the two vectors.

        """
        return Vector([x-y for x,y in zip(self.coordinates, other.coordinates)])

    def dot(self, other):
        """
        Computes the dot product of two vectors.

        Args:
            other (Vector): The other vector to compute the dot product with.

        Returns:
            float: The dot product of the two vectors.

        """
        return sum([x*y for x,y in zip(self.coordinates, other.coordinates)])

    def cross(self, other):
        """
        Computes the cross product of two vectors.

        Args:
            other (Vector): The other vector to compute the cross product with.

        Returns:
            Vector: A new vector representing the cross product of the two vectors.

        """
        if len(self.coordinates) != 3 or len(other.coordinates) != 3:
            raise ValueError("Both vectors must be 3-dimensional for cross product")
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates
        x = y1*z2 - y2*z1
        y = x2*z1 - x1*z2
        z = x1*y2 - x2*y1
        return Vector([x, y, z])

    def magnitude(self):
        """
        Computes the magnitude (length) of the vector.

        Args:
            None.

        Returns:
            float: The magnitude of the vector.
        return math.sqrt(sum([x**2 for x in self.coordinates]))
        """
    def normalize(vector):
    """
    Normalizes a given vector by dividing each element by the Euclidean length of the vector.

    Args:
        vector (list): A list of numbers representing the vector to be normalized.

    Returns:
        list: A list of numbers representing the normalized vector.

    """
    euclidean_length = sum([x**2 for x in vector]) ** 0.5
    return [x / euclidean_length for x in vector]
