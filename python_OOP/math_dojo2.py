class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *args):
        
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result += k
            else:
                self.result += i
        return self
    def sub(self, *args):
        
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result -= k
            else:
                self.result -= i
        return self

    def answer(self):
        print str(self.result)

math = MathDojo()
math.add(2,[23]).sub(3,4)
math.answer()