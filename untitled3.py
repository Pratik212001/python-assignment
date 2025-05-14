num=int(input('Enter the number'))

a=num

rev=0

while a>0:
      digit=a%10
      rev=rev*10+digit
      a=a//10
    
    
if num==rev:
      print("the number is palindrome")
else :
      print("the number is not palindrome")
     
# dry run 
 # a=121      121%10=1     0=0*10+1=1         num=121//10=12            
# a=12          12%10=2     1=1*10+2=12        num=12//10=1
# a=1           1%10=01     12=12*10+1=121     num=1//10=0
 
            #   121=121