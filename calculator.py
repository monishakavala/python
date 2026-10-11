n=int(input("enter n"))
a=float(input("enter a number"))
b=float(input("enter b number"))
if n==1:
    print("addition=",a+b)
elif n==2:
    print("subtraction=",a-b)
elif n==3:
    print("multiplication=",a*b)
elif n==4:
    if b!=0:
        print("division=",a/b)
    else:
        print("division by zero not possible")
else:
    print("invalid n")
