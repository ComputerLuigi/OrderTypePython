c1 = (0,0)
c2 = (1,1)
c3 = (1,2)

x1y2 = c1[0]*c2[1]
x1y3 = c1[0]*c3[1]
x2y3 = c2[0]*c3[1]
x2y1 = c2[0]*c1[1]
x3y1 = c3[0]*c1[1]
x3y2 = c3[0]*c2[1]

ordertype = x1y2 - x1y3 + x2y3 - x2y1 + x3y1 - x3y2  

print(ordertype* -1)

print(c1)
print(c2)
print(c3)

