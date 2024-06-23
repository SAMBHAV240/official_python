"""class person:
    __name = "anonymous"

    def __hello(self):
        print("Hello Person")

    def welcome(self):
        self.__hello() #hello ko andar chala skte hain bahar nhi

p1= person()
print(p1.welcome())"""

"""class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def stop():
        print("car stopped")

class toyotacar(Car):
    def __init__(self,name):
        self.name = name

car1= toyotacar("prius")
print(car1.type)"""

class person:
    name="anonymous"

    def changename(self,name):
        self.name=name
        #ye likh skte the tab shi rehta "person.name=name"
        #ya ye self.__class__.name = "sambhav"
        #ya fir class method use kre
    """(
          @classmethod
          def changename(cls,name)   #faltu hai koi need nhi
          cls.name=name              #isme First parameter cls aata hai self ki jagah
           )"""

c1=person()
c1.changename("sambhav")
print(c1.name)
print(person.name)