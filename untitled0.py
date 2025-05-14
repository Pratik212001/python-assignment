num=int(input("Enter the number"))

sum=0

a=num

while a>0:
     digit=a%10
     sum+=digit**3
     a//=10
    
if num==sum:
   print(num,"the number is armstrong number")
    
else:
    print(num,"the number is not armstrong number")    