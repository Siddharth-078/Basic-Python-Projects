# Higuruma emote counter = 0
import sys



n1 = input("Enter 1st Name ")
if (n1.isalpha() == False):
    print("Invalid Name Entered ")
    sys.exit()
f1 = int(input("Enter your order's price "))

n2 = input("Enter 2st Name ")
if (n2.isalpha() == False):
    print("Invalid Name Entered ")
    sys.exit()
f2 = int(input("Enter your order's price "))

n3 = input("Enter 3st Name ")
if (n3.isalpha() == False):
    print("Invalid Name Entered ")
    sys.exit()
f3 = int(input("Enter your order's price "))




tip = int(input("Enter Tip amount(0 if no Tip): "))
tax1 = (f1+f2+f3)*(5/100)

total = f1+f2+f3 + tip +tax1
#SPLITTING

Sp = input("Equal split(Type E) or Individual Split(Type I) ")


if(Sp == "E"):
    print('''================================
          BILL SUMMARY
================================''')
    
    print(n1.capitalize(),":" ,f1 )
    print(n2.capitalize(),":" ,f2 )
    print(n3.capitalize(),":" ,f3 )

    print("--------------------------------")

    print("Subtotal: ", (f1+f2+f3))
    total = int(total)


    print("Tax (5%): " ,int((f1+f2+f3)*(5/100)))
    print("Tip     : ", int(tip))

    print("--------------------------------")

    print("Total     : ", total)
    print("Split     : Equal")
    print("Per Person: ", int(total/3))

    print("================================")





if(Sp =="I"):
    print('''================================
          BILL SUMMARY
================================''')
    
    print(n1.capitalize(),":" ,f1 )
    print(n2.capitalize(),":" ,f2 )
    print(n3.capitalize(),":" ,f3 )

    print("--------------------------------")

    print("Subtotal: ", (f1+f2+f3))
    total = int(total)


    print("Tax (5%): " ,int((f1+f2+f3)*(5/100)))
    print("Tip     : ", int(tip))

    print("--------------------------------")

    print("Total     : ", total)
    m = tip/3
    n = tax1/3
    print("Split     : Individual")
    print(n1.capitalize() ,"pays",int(f1+m+n))
    print(n2.capitalize() ,"pays",int(f2+m+n))
    print(n3.capitalize() ,"pays",int(f3+m+n))

    


    # print("Sum: ", (f1+f2+f3))
