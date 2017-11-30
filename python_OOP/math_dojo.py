#Assignment: MathDojo
class MathDojo(object):
    def __init__(self,name):
        self.name = name
        self.result = 0
    def add(self,arr=None,arr2=None,num1=None,num2=None):
        if arr != None and type(arr) == list:
            for val in arr:
                self.result += val
        elif type(arr)==int:
            self.result += arr
        else:
            arr = None 
        if arr2 != None and type(arr2) == list:
            for val2 in arr2:
                self.result += val2
        elif type(arr2) == int:
            self.result += arr2
        else:
            arr2 = None
        if num1 != None and type(num1) == int:
            self.result += num1
        elif type(num1) == list:
            for val in num1:
                self.result += val
        else:
            num1 = None
        if num2 != None and type(num) == int:
            slef.result += num2
        elif type(num2) == list:
            for val in num2:
                self.result += val
        else:
            num2 = None
        return self

    def sub(self, arr=None, arr2=None, num1=None, num2=None):
        if arr != None and type(arr) == list:
            for val in arr:
                self.result -= val
        elif type(arr)==int:
            self.result -= arr
        else:
            arr = None 
        if arr2 != None and type(arr2) == list:
            for val2 in arr2:
                self.result -= val2
        elif type(arr2) == int:
            self.result -= arr2
        else:
            arr2 = None
        if num1 != None and type(num1) == int:
            self.result -= num1
        elif type(num1) == list:
            for val in num1:
                self.result -= val
        else:
            num1 = None
        if num2 != None and type(num) == int:
            slef.result -= num2
        elif type(num2) == list:
            for val in num2:
                self.result -= val
        else:
            num2 = None
        return self
        return self
    def answer(self):
        print self.result
        return self
math =  MathDojo("im adding")
math.add(5,5,[4,3,3]).sub(5,[1,2,2]).answer()
