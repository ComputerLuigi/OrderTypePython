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
c1 = (a[0],a[1])
c2 = (a[2],a[3])
c3 = (a[4],a[5])
d = list (pairwise(a))
d = d[0::2]
print (d)
z = ot.OrientedDoubleArea(c1,c2,c3)
print (z)
