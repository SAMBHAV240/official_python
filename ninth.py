"""class Circle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        print("area is:- ",(22/7)*self.radius**2)

    def Perimeter(self):
        print("perimeter is:- ",2*self.radius*(22/7))

c1=Circle(21)
c1.Area()
c1.Perimeter()"""


#INHERITANCE EXAMPLE
"""class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def show_details(self):
        print("Hi! Your details are :-","[Role-]", self.role,"[Department-]",self.dept,"[Salary-]",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Accountant","Finance",65000)

e1=Employee("Data Analyst","IT",70000)
e1.show_details()

engg1=Engineer("Sambhav",20)
engg1.show_details()"""


