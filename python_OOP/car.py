#Assignment: Car
class Car(object):
    def __init__(self,prize,speed,fuel,mileage):
        self.prize = prize
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12
    def display(self):
        print "Prize ",str(self.prize)
        print "Speed ",str(self.speed) + "mpg"
        print "Fuel ", str(self.fuel)
        print "Mileage " , str(self.mileage) + "mpg"
        if self.prize >= 10000:
            print "Tax ",str(0.15)
        else:
            print "Tax ",str(self.tax)

car1 = Car(2000, 35, 'Full', 15)
car2 = Car(2000, 5, 'Not Full', 105)
car3 = Car(2000, 15, 'Kind of Full', 95)
car4 = Car(2000, 25, 'Full', 25)
car5 = Car(2000, 45, 'Empty', 25)
car6 = Car(20000000, 35, 'Empty', 15)
new_car = Car(2000,"a lot ","Not full", "15")
new_car.display()
car1.display()
car2.display()
car3.display()
car4.display()
car5.display()
car6.display()

