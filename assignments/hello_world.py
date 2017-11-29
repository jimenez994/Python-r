print "Hello World"

print "this is a sample string"

name = "4"
print "My name is", name

print "My name is " + name

print "My name is "+name+""

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

hw = "hello %s" % 'world'
print hw
# the output would be:
# hello world

x = "Hello World"
print x.upper()
# output:
"HELLO WORLD"

x = [99, 4, 2, 5, -3]
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];

#loops
for count in range(0,5):
    print 'looping - ', count

count = 0 
while count < 5:
    print 'looping - ', count
    count += 1


