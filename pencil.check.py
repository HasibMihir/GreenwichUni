class pencil:
    def __init__(self,color,weight,length):
        def checktype(obj1,obj2):
            if not isinstance(obj1,obj2):
                print('invalid')
            else:
                print ('valid')
                return obj1
        self.__color=checktype(color,str)
        self.__weight=weight
        self.__length=length
        #####################color
    
    def set_color(self,color):
        if not isinstance(color,str):
            return "not a valid input"
        else:
            self.__color=color
            return 'valid'
    def getcolor(self):
        return self.__color
        ########################weight
    def set_weight(self,weight):
        if not isinstance(weight,int):
            return "not a valid input"
        else:
            self.__weight=weight
            return 'valid'
    def getweight(self):
        return self.__weight
        #########################length
    def set_length(self,length):
        if not isinstance(length,int):
            return "not a valid input"
        else:
            self.__length=length
            return 'valid'
    def getlength(self):
        return self.__length


mypencil=pencil(10,25,24)
print("color, weight and lengths are: ",mypencil.getcolor(),mypencil.getweight(),mypencil.getlength())
print(mypencil.set_length('hsid'))
print("color, weight and lengths are: ",mypencil.getcolor(),mypencil.getweight(),mypencil.getlength())

