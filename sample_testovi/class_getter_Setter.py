class Customer:
    
    def __init__(self, name, surname ):
        self.__FirstName = name
        self.__LastName = surname
        
    def getFirstName(self):
        return self.__FirstName
    def setFirstName(self, value):
        self.__FirstName = value


v=Customer('name', 'surname')

v.setFirstName("hello")

print(v.getFirstName())