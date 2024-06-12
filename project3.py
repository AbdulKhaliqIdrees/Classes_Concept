#concept of Accessor/Getter and Mutator/Setter
class Mobile():
    def __init__(self):
        self.price=28000
    def show(self):
        print("The Price of Mobile is",self.price)
    def get_price(self): #Getter/Accessor Method
        return self.price
    def set_price(self): #Mutator/Setter Method
        self.price=50000
        print("Run Mutator/Setter Method",self.price)
    def showw(self):
        print("The Price of Mobile is",self.price)


a=Mobile()
a.show()
print("The Price Befor Modification",a.price)
v=a.get_price() #Run Getter/Accessor Method By Object
print("Reurn Value From Getter/Accessor Method=",v)
print("The Price Befor Modification",a.price)
a.set_price()  #Run Mutator/Setter Method by Object
print("The Price After Modification",a.price)
a.showw()
