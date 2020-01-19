total=0
for number in [1,2,3,4,5,6,7,8,9,10]:
    num=input("Enter #" + str(number) +": ")
    total = float(total) + num

average = total / 10.0
print
print "  Total =", int(total)
print "Average =", average