import OrderType as ot
import ReadInput as ri


def func(x):
    return x * 5


def test_answer():
    assert func(5) == 25


def test_colinear():
    assert ot.OrientedDoubleArea((0, 0), (1, 1), (2, 2)) == 0


def test_right_handed_triangle():
    assert ot.OrientedDoubleArea((0, 0), (1, 1), (3, 2)) > 0


def test_left_handed_triangle():
    assert ot.OrientedDoubleArea((0, 0), (1, 1), (2, 3)) < 0


def test_colinear_ot():
    a = ri.CoordinateCombinations([(0, 0), (1, 1), (2, 2)])
    assert ri.ListOrderTypes(a) == [0]


def test_coordinate_packer():
    a = [1, 2, 3, 4, 5, 6]
    import ReadInput as ri
    assert ri.MakeCoordinateList(a) == [(1, 2), (3, 4), (5, 6)]
