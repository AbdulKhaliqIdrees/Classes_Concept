#Concept of Static Method With or WithOut Parameters
class Mobile(object):
    price=48000
    @staticmethod #Decorator
    def show(c,m="VivoY21"): #Static Method do not Take First Parameter like "self" and "cls".
        color=c
        model=m
        print("Price of Mobile is",Mobile.price)
        print("Color of Mobile is",color)
        print("Model of Mobile is",model)
a=Mobile()
b=Mobile()
a.show("Blue","VivoY20")  
print()
b.show("Yellow")
print()
Mobile.show("Red","Redmi")         
