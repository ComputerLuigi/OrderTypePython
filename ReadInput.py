a = []
with open( 'input' ) as f:


	for line in f:
		words = line.split(',')
		b = (int(words[0]),int(words[1]))
		a += tuple(b)
print (a[2])
