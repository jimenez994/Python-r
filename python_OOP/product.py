#Assignment: Product
class Product(object):
    def __init__(self,prize,item_name,weight,brand):
        self.prize = prize
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self 
    def add_tax(self,tax):
        print tax * 100 ,"%"
        self.prize = self.prize * tax + self.prize
        return self
    def returm(self,reason):
        if reason == "damage":
            self.status = "Defected"
            self.prize = 0
        elif reason == "unopened":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.prize = self.prize - self.prize * 0.2 
        return self
    def display_info(self):
        print "Prize "+ str(self.prize)
        print "Item "+ str(self.item_name)
        print "Weight "+ str(self.weight) + " grams"
        print "Brand " + str(self.brand)
        print "Status " + str(self.status)
product = Product(2000,"iphone",20,"apple")
product.sell()
product.add_tax(0.06).add_tax(0.08)

#return reasons
#damage
#unopened
#opened
product.returm("opened")
product.display_info()
