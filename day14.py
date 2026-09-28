# If Else
print(' {Type Casting} ')

# (Conditions Operaters)
# >, <, >=, <=, ==,
a=int(input("Enter your age "))
print("Your age is:",a)

if(a>18):#a 18 se bara hai tu if
    print('You can drive')
else:
    print('You can not drive')
# 
applPrice=210
budget=200
if(applPrice<=budget):
    print("Alexa, add 1 kg Apples to the card")
else:
    print("Alexa, do not add Apples to the card")
# 
b=10
c=200
print("()")
if(c-b >50):
   print("Alexa, add 1 kg Apples to the card")
elif(c-b >70):
    print("It's oKay you can buy")
else:
    print("Alexa, do not add Apples to the card")

# 
num=int(input("Enter Your Number "))
if(num<0):
    print('Number is negative')
elif(num==0):
    print('Number is zero')
elif(num==999):
    print("Number is special")

else:
    print("Number is positive")