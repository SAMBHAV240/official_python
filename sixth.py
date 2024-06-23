"""class Student:
    language_name="PYTHO"

    def __init__(self,name,marks): #parametrized contructor
        self.name=name
        self.marks=marks
    
    @staticmethod
    def hello():
        print("Hi babe! How are you?")

    def get_average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hello,",self.name,"your average score is",sum/3)

s1= Student("Sambhav",[96.7,95.6,98.9])
s1.get_average()        
s1.hello()"""


#PRACTICE QUESTION
class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no

    def debit(self,amount_debited):
        self.balance-=amount_debited
        print("here is you amount debited:- ₹",amount_debited)
        print("Total Balance is:- ₹",self.get_balance())

    def credit(self,amount_credited):
        self.balance+=amount_credited
        print("here is you amount credited:- ₹",amount_credited)
        print("Total Balance is:- ₹",self.get_balance())

    def get_balance(self):
        return self.balance
    

acc1=Account(9975,6390)
acc1.debit(375)
acc1.credit(369)
