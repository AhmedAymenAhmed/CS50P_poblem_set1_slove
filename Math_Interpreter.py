#we will ask the user to input 1st and 2nd numbers and the operation he want 
x=input("Enter the first number ")
y=input("Enter the operation (+)\ (-) \ (*) \ (/)")
z=input("Enter the second number ")
#do the operation
try :
    if y=="+" :
        result=float(x) + float(z)
    elif y=="-" :
        result=float(x) - float(z)
    elif y=="*" :
        result=float(x) * float(z)
    elif y=="/" :
        result=float(x) / float(z)
    else :
        print("invalid input")
except ValueError:
    print("Invalid input")
if int(result)==float(result):
    result =int(result)

print (f"the result is{result}")