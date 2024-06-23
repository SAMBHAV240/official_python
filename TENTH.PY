# GUESS THE NUMBER MINI PROJECT
import random

target= random.randint(1,100)

while True:
    userChoice=input("Guess the target or Quit the game :-")
    if(userChoice =="quit"):
        break

    userChoice=int(userChoice)
    if(userChoice==target):
        print("Le Betee Moj Krdii")
        break

    elif(userChoice < target):
        print("Isse thoda sa bada hai bas")

    else:
        print("Isse thoda sa chota hai bas")

print("Game Khatam Apne Apme Ghar Holo")


#RANDOM PASSWORD GENERATOR

"""import random
import string

TotalValues = string.ascii_letters + string.digits + string.punctuation
#a=len(string.punctuation) 
# 26+26+10+32
password_len=12
print(TotalValues)
print(len(TotalValues))

passWord = ""
for i in range(password_len):
    passWord += random.choice(TotalValues)

#ek or method hai vo vaise mrko bakr lgta hai but chal skta hai
#through LIST COMPREHENSION(FUNCTION KO BAA AAR CALL KRAKE VALUES KO LIST KI FORM ME STROE KRNA)

    result= .join[random.choice(TotalValues) for i in range(password_len)]
    print(result)
    bas ab list ki form  me aajenge or .join lgake join hojenge
    .join se pehle agar kuch daldiya to sari values usi chix se seprate hojengi jaise comma
"""


#print("Your random password is:- ",passWord)"""
