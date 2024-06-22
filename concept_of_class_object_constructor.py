#Learn Concept of Class,Object,Constructor,instance Variable,instance method,Local variable,Foramal and actual arguments 
class Mobile(object): # Written "object" is Optional.This Shows that this Class is inherited From Object Class 
    def __init__(self,color):  #Constructor
        self.price=23000             #instance Variable
        self.model="VivoY21"         #instance Variable
        self.color=color             #instance Variable
    def show(self,v):            #instance Method
        memory=64              #Local Variable witout Self
        self.camera=v          #Local Variable With Self
        print("The Price of Mobile is",self.price,"Rs.")  #Accessing instance Variable inside the Class
        print("The Modelof Mobile is",self.model)         #Accessing instance Variable inside the Class
        print("The Color of Mobile is",self.color)        #Accessing instance Variable inside the Class
        print("The Memory of Mobile is",memory,"Bits")    #Accessing Local Variable inside the Class
        print("Is Mobile have Camera",self.camera)        #Accessing Local Variable inside the Class
a=Mobile("Blue and Orange")  #Formation of Object and Passing Actual Arguments
a.show("Yes") #Print Insance Method By using Object  
print(a.price) #Print Instance Variable out of the class by using Object 
print(a.model) #Print Instance Variable out of the class by using Object
print(a.color) #Print Instance Variable out of the class by using Object
print(a.camera) #Print Local Variable out of the class by using Object

