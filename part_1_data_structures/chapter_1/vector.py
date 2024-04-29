import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Returns a string representation of the Vector object.
        For more information on the difference between __str__ and __repr__,
        refer to the documentation at https:///fpy.li/1-5
        """
        return f"Vector({self.x!r}, {self.y!r})"

    # def __str__(self):
    #     return f"Vector({self.x}, {self.y})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        """
        Returns True if the Vector object has non-zero components, otherwise False.
        Refer to the commented method below for more details on why this implementation is faster.
        """
        return bool(self.x or self.y)

    def __bool__(self):
        """
        Provides a slower implementation of __bool__.

        To comprehend the runtime differences, copy the code snippet from `file_name.txt` to an online visualized debugger.
        My recommendation is: https://pythontutor.com/python-compiler.html
        Remember to adjust the debugger settings to use Python 3.11.
        """
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    v0 = Vector()
    v1 = Vector(4, 3)
    v2 = v1 + v1
    v3 = v1 * 2
    print(v1, abs(v1))
    print()
    print(v2, abs(v2))
    print()
    print(v3, abs(v3))
    print()
    print(abs(v3) == abs(v2))
    v4 = Vector('2', '3')
    print(">>> ", v2 and v0)

    # for _ in range(100_000_000):
    #     bool(v0)
    #     bool(v1)
