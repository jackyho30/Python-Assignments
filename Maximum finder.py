def maximum(a,b,c):
    if a > b and a > c:
        greatest = a
    elif b > a and b > c:
        greatest = b
    else:
        greatest = c
    return greatest #assigns value to function

a = input ("Enter 1st number: ")
b = input ("Enter 2nd number: ")
c = input ("Enter 3rd number: ")
maximum(a,b,c) #calls function
greatest = maximum(a,b,c)
print "The largest is", greatest
