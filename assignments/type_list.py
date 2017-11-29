l = ['magical unicorns',19,'hello',98.98,'world']
t = [2, 3, 1, 7, 4, 12]
g = ['magical', 'unicorns']

def arr_list (myArray):
    message = " "
    sum = 0
    
    for count in range(0,len(myArray)):
        if type(myArray[count]) is str:
            message += myArray[count]
            message += " "
        if type(myArray[count]) is int or type(myArray[count]) is float:
            sum += myArray[count]
    if message != " " and sum != 0:
        print "This list you entered os of mixed type"
        print "String", message
        print "Sum:", sum
    elif sum != 0 and message == " ":
        print "The list you entered is of integer type"
        print "Sum:", sum
    else:
        print "The list you entered is of string type"
        print "String", message
    
arr_list(g)
