# Math Case

# import os
# print("Hellow world from")
# os.system("Python --version")

x=int(input("Enter the value of x: "))
match x:

 # if  x is 0
    case 0:
        print("x is zero")

# case with if-condition
    case 8:
        print("case is 78")

    case _ if x==33:
        print("The value of x is:33")
    case _ if x>15:  
        print("The value of x is graeter than")
    case _ if x<6:
        print("The value of x is less than")
    case _:
        print(x)