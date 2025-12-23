class Student:
    def __init__(self):
        self.__bal=10000
    @property
    def bal(self):
        return self.__bal
    @bal.setter
    def bal(self,new_bal):
        self.__bal=new_bal
        
s = Student()
print(s.bal)
s.bal = 20000
print(s.bal)