numbers=[31,48,60,20,10]
for i in numbers:
    if(i%2==0):
        print(i,"even numbers")
total=sum(numbers)
average=total/len(numbers)
print("sum=",total)
print("average=",average)
