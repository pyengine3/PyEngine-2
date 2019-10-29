import math


class Vec2:
    def __init__(self, x, y):
        """
            Create Vec2 Object

            :param x: X Coord
            :param y: Y Coord
        """
        self.x = x
        self.y = y

    def coords(self):
        """
            Return a tuple of coords

            :return: Tuple with X and Y Coords
        """
        return self.x, self.y

    def set_coords(self, x, y):
        """
            Define X and Y Coords

            :param x: X Coord
            :param y: Y Coord
        """
        self.x = x
        self.y = y

    def normalized(self):
        """
            Return the normalized Vector created with the vector

            :return: Normalized Vector
        """
        if len(self) == 0:
            return Vec2.zero()
        else:
            return Vec2(int(self.x / len(self)), int(self.y / len(self)))

    def __len__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        else:
            return Vec2(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        else:
            return Vec2(self.x - other, self.y - other)

    def __rsub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(other.x - self.x, other.y - self.y)
        else:
            return Vec2(other - self.x, other - self.y)

    def __mul__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        else:
            return Vec2(self.x * other, self.y * other)

    def __truediv__(self, other):
        if isinstance(other, Vec2):
            return Vec2(int(self.x / other.x), int(self.y / other.y))
        else:
            return Vec2(int(self.x / other), int(self.y / other))

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return "Vec2" + str((self.x, self.y))

    def __eq__(self, other):
        return other is not None and self.x == other.x and self.y == other.y

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    @classmethod
    def zero(cls):
        """
            Return the Vector Zero

            :return: Vector Zero
        """
        return Vec2(0, 0)
