# 1
def print1to255():
	for i in range(1,256):
		print i

# 2
def printOdds1to255():
	for i in range(1,256,2):
		print i

# 3
def printIntsAndsSums255():
	sum = 0
	for i in range(1,256):
		sum += i
		print i, sum
	
# 4
def iterateAndPrintList(arr):
	for i in range(len(arr)):
		print arr[i]
	# for element in arr:
	# 	print element

# 5
def printMax(arr):
	max = arr[0]
	for val in arr:
		if val > max:
			max = val
	print max

# 6
def printAverage(arr):
	sum = arr[0]
	for var in range(1, len(arr)):
		sum += arr[var]
	print sum / float(len(arr))

# 7
def arrayOdds1to255():
	arr = []

	for i in range(1,256):
		if i%2 != 0:
			arr.append(i)

	print arr

	# print range(1,256,2)

# 8
def squareValues(arr):
	for i in range(0,len(arr)): 
		arr[i] = arr[i]**2
	print arr

# 9
def countGreaterThanY(arr, y):
	count = 0
	for i in range(len(arr)):
		if arr[i] > y:
			count +=1
	print count

# 10
def zeroNegativeValues(arr):
	for i in range(len(arr)):
		if arr[i] < 0:
			arr[i]=0
	print arr 

# 11
def minMaxAverage(arr):
	min = arr[0] 
	max = arr[0]
	sum = 0
	for i in range(len(arr)):
		sum+=arr[i]
		if arr[i]>max:
			max=arr[i]
		if arr[i]<min:
			min=arr[i]
	print min, max, sum/float(len(arr))

# 12
def shiftArrayValuesToLeft(arr):
	for i in range(len(arr)-1):
		arr[i]= arr[i+1]
	arrm
def swapStringForNegatives(arr, string):
	for i in range(len(arr)):
		if arr[i]< 0:
			arr[i]=string
	print arr

# 14
def sumValuesFrom0toN(n):
	sum =0
	for i in range(0,n+1):
		sum =sum+i
	print sum
# 15
def convertFarenheitToCelcius(f):
	print (f*(5/9))- 32

# 16
def pushFront(arr, val):
	arr.append(0)
	for i in range(len(arr)-1,0,-1):
		arr[i] = arr[i-1]
	arr[0] = val
	print arr

# 17
def arrayReverse(arr):
	for i in range(len(arr)/2):
		temp=arr[i]
		arr[i]=arr[len(arr)-1-i]
		arr[len(arr)-1-i]=temp
	print arr

# 18
def stringReverse(string):
	new_string = ""
	for i in range(len(string)-1, -1, -1):
		new_string += string[i]
	print new_string	

# 19 
def characterCount(sentence):
	count = 0
	for i in range (0,len(sentence)):
		if not sentence[i].isspace():
			count += 1
	print count

arr = [22, 5, 17, -3, 0, -2, -1, 60, 64, -8]
string = "Coding Dojo"
sentence = " Lorem ipsum   dolor sit  amet! "

# print1to255()
# # printOdds1to255()
# printIntsAndsSums255()
# iterateAndPrintList(arr)
# # printMax(arr)
# printAverage(arr)
# # arrayOdds1to255()
# squareValues(arr)
# countGreaterThanY(arr, 16)
# zeroNegativeValues(arr)
# minMaxAverage(arr)
# # shiftArrayValuesToLeft(arr)
# swapStringForNegatives(arr, string)
# sumValuesFrom0toN(8)
# convertFarenheitToCelcius(212)
# pushFront(arr, 7)
# # arrayReverse(arr)
# stringReverse(string)
characterCount(sentence)