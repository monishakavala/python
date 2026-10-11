n=int(input("enter a number"))
s=0
for i in range(1,n+1):
    if(i%2==0):
        print("odd:::",i)
    else:
        print("even:::",i)
    s=s+i
print("sum is:::",s)
