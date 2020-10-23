import OrderType as ot
import itertools as it


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)

def makeCoordinateList():
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

def ListOrderTypes(e):
	x = []
	for triple in iter(e):
		x.append(ot.OrientedDoubleArea(triple[0],triple[1],triple[2]))
	return x	

print(ListOrderTypes(CoordinateCombinations(makeCoordinateList())))
