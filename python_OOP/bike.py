#Assignment: Bike
class Bike(object):
    
    def __init__(self,price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Price is: $" + str(self.price)
        print "Maximum Speed: " + str(self.max_speed)
        print "Miles: " + str(self.miles)
    def ride(self):
        print "Riding"
        self.miles += 10
        print "Miles " + str(self.miles)
    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
            print "Miles " + str(self.miles)
new_bike = Bike("200","350")
new_bike.displayInfo()
new_bike.ride()
new_bike.ride()
new_bike.ride()
new_bike.reverse()



