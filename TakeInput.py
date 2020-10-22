import OrderType as ot 
val1 = int(input("Enter the x1 coordinate "))
val2 = int(input("Enter the y1 coordinate "))
val3 = int(input("Enter the x2 coordinate "))
val4 = int(input("Enter the y2 coordinate "))
val5 = int(input("Enter the x3 coordinate "))
val6 = int(input("Enter the y3 coordinate "))
c1 = (val1, val2)
c2 = (val3, val4)
c3 = (val5, val6)

output=ot.OrientedDoubleArea(c1,c2,c3)
print (output)






