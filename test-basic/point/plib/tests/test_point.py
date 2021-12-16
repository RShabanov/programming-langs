import pytest
from plib import Point, PointError

@pytest.fixture
def points():
    return Point(1, 2), Point(2, 2)

class TestPoint:

    def test_creation(self):
        p = Point(1, 2)
        assert p.x == 1 and p.y == 2

        p = Point(1.5, 1.5)
        assert p.x == 1.5 and p.y == 1.5
        
        with pytest.raises(PointError): Point("a", 10)

    def test_addition(self, points):
        p1, p2 = points
        assert p1 + p2 == Point(3, 4)

    def test_subtract(self, points):
        p1, p2 = points
        assert p1 - p2 == Point(-1, 0)

    @pytest.mark.parametrize(
        "p1, p2, distance",
        [
            (Point(0, 0), Point(0, 10), 10),
            (Point(0, 0), Point(10, 0), 10),
            (Point(0, 0), Point(10, 10), 14)
        ]
    )
    def test_distance_all_axis(self, p1, p2, distance):
        assert p1.distance_to(p2) == pytest.approx(distance, 1)

    def test_eq_with_other_type(self):
        p = Point(0, 0)
        with pytest.raises(NotImplementedError):
            p == 0