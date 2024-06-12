#Concept of More than One Objects and Class Variables
class Mobile():
    memory=64   #Class Variable
    def __init__(self):
        self.model="Vivo"
        self.color="Yellow"
    def show(self):
        print("Mobile Model",self.model)
        print("Mobile Color",self.color)
        print("Mobile Memory",self.memory)
    @classmethod #Decorator
    def showw(cls,p):
        cls.price=p
        print("Mobile Memory",cls.memory)
        print("Mobile Price",cls.price)
a=Mobile() #Object Formation
b=Mobile() #Object Formation
c=Mobile() #Object Formation
a.show()   #Print Instance Metod By Object
print()
b.show()   #Print Instance Metod By Object
print()
c.show()   #Print Instance Metod By Object
print()
Mobile.show(a) #Print Instance Metod By Class
print()
#Print Instance and Class Variables Outside the Class By Object
print(a.memory)  
print(a.color)
print(a.model) 
print()
print(Mobile.memory) #Print Class Variable Outside the Class By Class
print()
a.showw(23000) #Run Class Method By Object
print()
Mobile.showw(2300) #Run Class Method By Class
#Modification with Objects
#Modification in only Object b
b.color="Blue"
b.memory=67 
#After Modifaction
print()
a.show()
print()
b.show()
print()
c.show()
#Modification With Class
Mobile.memory=100
#After Modifaction
print()
a.show()
print()
b.show()
print()
c.show()
