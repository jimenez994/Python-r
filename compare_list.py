#Compare List
one = [1, 2, 5, 6, 2]
two = [1, 2, 5, 6, 2]

# one = [1, 2, 5, 6, 5]
# two = [1, 2, 5, 6, 5, 3]

# one = [1, 2, 5, 6, 5, 16]
# two = [1, 2, 5, 6, 5]

# one = ['celery', 'carrots', 'bread', 'milk']
# two = ['celery', 'carrots', 'bread', 'cream']

def compare (list_one,list_two):
    check = True
    if len(list_one) == len(list_two):
        for count in range (0,len(list_one)):
            if list_one[count] != list_two[count]:
               check = False 
    else:
        check = False
    if check == True:
        print "The lists are the same"
    else:
        print "The lists are not the same"
compare(one,two)
