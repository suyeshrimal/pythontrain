class Person:
    def __init__(self,name,age,password) -> None:
        self.name=name  #public
        self._age=age   #protected
        self.__password=password   #private
#private chai class bahira access garna mildeina
    def get_password(self):
        return self.__password
    
    def set_password(self,password):
        self.__password=password


    password=property(get_password,set_password)

person=Person('ram',12,'passw123')
print(person.name)
print(person._age)
person.password=123
print(person.password)