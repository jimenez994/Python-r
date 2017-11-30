#Assignment: Animal

class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def status(self):
        print self.name
        print self.health
        return self

class Dog(Animal):
    def __init__(self,name):
        self.name = name
        self.health = 150
    def inc_health(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self,name):
        self.name = name
        self.health = 170
    def fly(self):
        self.health -=10
        return self
    def display_health(self):
        print "I im a Dragon!"
        print self.name 
        print self.health
cow = Animal("max",100)
max = Dog("Maximus")
gragon = Dragon("Drogo")
cow.walk()
cow.run()
cow.status()
max.inc_health().inc_health()
max.walk().walk().walk().run().run().status()

gragon.fly().display_health()
