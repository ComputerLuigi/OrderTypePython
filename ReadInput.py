import OrderType as ot
import itertools as it

a = []

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)

with open( 'input' ) as f:
	for line in f:
		words = line.split(',')
		b = (int(words[0]),int(words[1]))
		a += (b)

d = list (pairwise(a))
d = d[0::2]

e = list(it.combinations(d,3))

for triple in e:
	x = ot.OrientedDoubleArea(triple[0],triple[1],triple[2])
	print (x)
