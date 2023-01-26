class pencil:
    def __init__(self,weight,color,length):
        self.__weight=weight
        self.__color=color
        self.__length=length
    def getweight(self):
        return self.__weight
    def getcolor(self):
        return  self.__color
    def getlength(self):
        return self.__length
        
    def setweight(self,value1):
         self.__weight=value1
    def setcolor(self,value2):
        self.__color=value2
    def setlength(self,value3):
        self.__length=value3
    
a= pencil(12,'red',14)
print("weight of the pencil is: ", a.__weight())
print("COLOR of the pencil is: ", a.getcolor())
print("length of the pencil is: ", a.getlength())
print("weight, color and length of the pencil are: ", a.getweight(),a.getcolor(),a.getlength())