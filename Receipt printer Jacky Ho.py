subtotal = input ("Enter the bill subtotal $") 

HST = subtotal * 0.13

Tip = int (subtotal * 0.15)

Total = subtotal + HST + Tip

line1 = "13% HST: $"

line2 = "Tip: $"

line3 = "TOTAL: $"

print "  YOUR RECEIPT"

print 

print "="*17

print "Subtotal: $%6.2f" % subtotal

print "%11s%6.2f" % (line1, HST)

print "%11s%6.2f" % (line2, Tip)

print "="*17

print "%11s%6.2f" % (line3, Total)
 
print 

print "THANK YOU!"