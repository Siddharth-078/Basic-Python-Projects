# higurama emote count = 2
import sys




name = input("Enter your name: ")
if(name.replace(" ", "").isalpha() == False):
    print("Invalid name Entered")
    sys.exit()


age = int(input("Enter your age: "))
if(((age < 0) or  (age > 120))  ):
    print("Invalid Age Entered")
    sys.exit()


ph = (input("Enter your Phone number: "))
if((len(ph) != 10) or (ph.isdigit() == False)):
    print("Invalid Phone Number Entered")
    sys.exit()


email = (input("Enter your Email: "))
email1 = email.lower()


hb = [input("Enter Hobbie 1: "), input("Enter Hobbie 2: "), input("Enter Hobbie 3: ")]

hb.sort()



print('''========================
       CONTACT CARD
========================''')
print("Name    :",name)
print("Age     :",age)
print("Phone   :",ph)
print("Email   :", email1)
print("Hobbies :", hb[0], hb[1], hb[2])










        
