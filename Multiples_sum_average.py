for count in range(1,1000,2):
    print "odd - ", count
#odd Numbers

for multiples in range(5,100,5):
    print "multiples ", multiples
#multiples of 5

x = [1, 2, 5, 10, 255, 3]
sum = 0 

for e in range (0,len(x)-1):
    sum += x[e]
print "sum - ", sum
#sum list

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in range (0,len(a)-1):
    sum += a[i]
print "average", sum/len(a)
#average list

