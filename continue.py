s=input("enter a string").lower()
l=len(s)
for i in range(1,l):
      if(s[i]!=s[l-i-1]):
        print("not palindrome")
print("palindrome")

         
