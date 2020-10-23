import OrderType as ot
import itertools as it


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)

def makeCoordinateList():
	##reads a file with one x,y pair per line and returns a list of tuples [(x1,y1)...(xn,yn)]
	a = []
	with open( 'input' ) as f:
		for line in f:
			words = line.split(',')
			b = (int(words[0]),int(words[1]))
			a += (b)

	d = list (pairwise(a))
	d = d[0::2]
	return d

def CoordinateCombinations(d):
	e = (it.combinations(d,3))
	return e

def ListOrientedDoubleAreas(e):
	x = []
	for triple in iter(e):
		x.append(ot.OrientedDoubleArea(triple[0],triple[1],triple[2]))
	return x	


def ListOrderTypes(e):
	x = []
	for triple in iter(e):
		b = (ot.OrientedDoubleArea(triple[0],triple[1],triple[2]))
		if b != 0:
			x.append(b / abs(b))
		else:
			x.append(0)
	return x	


def CountColinear(f):
	a = 0
	for i in f:
		if i == 0:
			a += 1
	return a
			
		
		

a = (ListOrderTypes(CoordinateCombinations(makeCoordinateList())))
print (a)
print ("Number of colinear triples: " + str(CountColinear(a)))
