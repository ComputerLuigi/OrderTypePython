a = []
with open( 'input' ) as f:


	for line in f:
		words = line.split(',')
		b = (int(words[0]),int(words[1]))
		a += tuple(b)
import OrderType as ot
c1 = (a[0],a[1])
c2 = (a[2],a[3])
c3 = (a[4],a[5])

z = ot.OrientedDoubleArea(c1,c2,c3)
print (z)
