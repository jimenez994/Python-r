"""
Assignment: Call Center
You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

You will create two classes. One class should be Call, the other CallCenter.

Call Class
 Create your call class with an init method. Each instance of Call() should have:
Attributes:

 unique id

 caller name

 caller phone number

 time of call

 reason for call
Methods:

 display: that prints all Call attributes.
CallCenter Class
 Create your call center class with an init method. Each instance of CallCenter() should have the following attributes:
Attributes:

 calls: should be a list of call objects

 queue size: should be the length of the call list
Methods:

 add: adds a new call to the end of the call list

 remove: removes the call from the beginning of the list (index 0).

 info: prints the name and phone number for each call in the queue as well as the length of the queue.
You should be able to test your code to prove that it works. Remember to build one piece at a time and test as you go for easier debugging!

""" 
from datetime import datetime

class Call(object):
	def __init__(self,id,name,number,reason):
		self.id = id
		self.name = name
		self.number = number 
		self.reason = reason 
		self.time = datetime.now()

	def displayInfo(self):
		print self.id, self.name, self.number, self.reason, self.time
		return self

	def __repr__(self):
		return "{} {}".format(self.name, self.number)

class Callcenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = 0
	def add(self, call):
		self.calls.append(call)
		self.queue_size += 1
		return self
	def remove(self):
		del self.calls[0]
		self.queue_size -=1
		return self
	def info(self):
		print "there are ",self.queue_size,"waiting"
		for call in self.calls:
			call.displayInfo() 
		return self

call1 = Call("123","Ghostbusters", "123-4567", "there's a ghost")
call2 = Call("124","Ghosts", "123-4568", "there's a ghostbuster")
center1 = Callcenter()
center1.add(call1).add(call2).info().remove().info()