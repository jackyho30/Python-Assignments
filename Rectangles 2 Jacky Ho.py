#RECTANGLES

width_1 = input ("Enter width of rectangle #1: ")
length_1 = input ("Enter length of rectangle #1: ")
width_2 = input ("Enter width of rectangle #2: ")
length_2 = input ("Enter length of rectangle #2: ")

area_1 = width_1 * length_1
area_2 = width_2 * length_2

if area_1 > area_2:
	print "Rectangle #1 has the greatest area."
elif area_1 < area_2:
	print "Rectangle #2 has the greatest area."
else:
	print "Rectangle #1 and #2 have the same area."