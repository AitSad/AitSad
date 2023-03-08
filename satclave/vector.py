import math

class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __str__(self):
        return f"Vector: {self.coordinates}"

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __add__(self, other):
        return Vector([x+y for x,y in zip(self.coordinates, other.coordinates)])

    def __sub__(self, other):
        return Vector([x-y for x,y in zip(self.coordinates, other.coordinates)])

    def dot(self, other):
        return sum([x*y for x,y in zip(self.coordinates, other.coordinates)])

    def cross(self, other):
        if len(self.coordinates) != 3 or len(other.coordinates) != 3:
            raise ValueError("Both vectors must be 3-dimensional for cross product")
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates
        x = y1*z2 - y2*z1
        y = x2*z1 - x1*z2
        z = x1*y2 - x2*y1
        return Vector([x, y, z])

    def magnitude(self):
        return math.sqrt(sum([x**2 for x in self.coordinates]))

    def normalize(self):
        mag = self.magnitude()
        return Vector([x/mag for x in self.coordinates])
