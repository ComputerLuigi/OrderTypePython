def func(x):
	return x * 5

def test_answer():
	assert func(5) == 25

import OrderType as ot 

def test_another():
	assert ot.OrientedDoubleArea((0,0),(1,1),(2,2)) == 0

def test_right_handed_triangle():
	assert ot.OrientedDoubleArea((0,0),(1,1),(3,2)) > 0
	
def test_left_handed_triangle():
	assert ot.OrientedDoubleArea((0,0),(1,1),(2,3)) < 0
