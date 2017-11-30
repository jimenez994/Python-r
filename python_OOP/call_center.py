#call Center
from datetime import datetime 
class Call(object):
    def __init__(self,id,name,number,reason):
        self.id = id
        self.name = name
        self.number = number
        self.reason = reason
        self.time = datetime.now() 
    def display(self):
        print self.id,self.name, self.number, self.reason, self.time
        return self
    def __repr__(self):
        return "{}" "{}".format(self.name,self.number)
class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0
    def add(self,call):
        self.calls.append(call)
        self.queue += 1
        return self
    def remove(self):
        del self.calls[0]
        self.queue -=1
        return self
    def info(self):
        print self.queue
        for call in self.calls:
            call.display()
        return self


call1 = Call("123","Ghostbusters", "123-4567", "there's a ghost")
call2 = Call("124","Ghosts", "123-4568", "there's a ghostbuster")
center1 = CallCenter()
center1.add(call1).add(call2).info().remove().info()
