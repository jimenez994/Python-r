#Assignment: Fun with Functions
#odd/even
def odd_even (star,end):
    for i in range (star,end):
        if i % 2 == 0:
            print "Number is ", i, ".  This is an even number."
        else:
            print "Number is ", i, ".  This is an odd number."

odd_even(0,2)

#multiply
def multiply(arr, num):
    for x in range(0, len(arr)):
        arr[x] *= num
    return arr
numbers_array = [3, 6, 8, 10, 67]

print multiply(numbers_array, 5)

#Hacker Challenge:


def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0, x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array


x = layered_multiples(multiply([2, 4, 5], 3))
print x
# output
