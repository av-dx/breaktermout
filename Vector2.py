import math


class Vector2:

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = round(x, 5)
        self.y = round(y, 5)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def __neg__(self) -> "Vector2":
        return (Vector2(-self.x, -self.y))

    def __add__(self, other: "Vector2") -> "Vector2":
        return (Vector2(round(self.x+other.x, 5), round(self.y+other.y, 5)))

    def __sub__(self, other: "Vector2") -> "Vector2":
        return (self + (-other))

    def __mul__(self, c: float) -> "Vector2":
        return (Vector2(round(self.x * c, 5), round(self.y * c, 5)))

    def __truediv__(self, c: float) -> "Vector2":
        if (c == 0):
            print("DIVISION BY ZERO!")
            input()
            return nullVector2
        else:
            return (Vector2(round(self.x / c, 5), round(self.y / c, 5)))

    def __eq__(self, other: "Vector2") -> bool:
        return (self.x == other.x and self.y == other.y)

    def __lt__(self, other: "Vector2") -> bool:
        return (self.x < other.x and self.y < other.y)

    def __gt__(self, other: "Vector2") -> bool:
        return (self.x > other.x and self.y > other.y)

    def __ge__(self, other: "Vector2") -> bool:
        return (self.x >= other.x and self.y >= other.y)

    def __le__(self, other: "Vector2") -> bool:
        return (self.x <= other.x and self.y <= other.y)

    def dot(self, other: "Vector2") -> "Vector2":
        return (self.x*other.x + self.y*other.y)

    def __floor__(self) -> "Vector2":
        return (Vector2(math.floor(self.x), math.floor(self.y)))

    def __ceil__(self) -> "Vector2":
        return (Vector2(math.ceil(self.x), math.ceil(self.y)))

    def __round__(self) -> "Vector2":
        return (Vector2(round(self.x), round(self.y)))


nullVector2 = Vector2(0, 0)
