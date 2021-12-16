from typing import Union

class Point:

    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise PointError("x, y should be an integer type")
        self.x = x
        self.y = y

    def __add__(self, other: "Point") -> "Point":
        return Point(
            x=self.x + other.x, 
            y=self.y + other.y
            )

    def __sub__(self, other: "Point") -> "Point":
        return Point(
            x=self.x - other.x, 
            y=self.y - other.y
            )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            raise NotImplementedError
        return self.x == other.x and self.y == other.y

    def distance_to(self, other: "Point") -> float:
        p = self - other
        return (p.x ** 2 + p.y ** 2) ** 0.5


class PointError(Exception):
    ...