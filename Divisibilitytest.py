# bike problem

price=float(input("Enter the price of a bike"))

if price>80000:
   tax=(15/100)*price
   totalprice=price+tax
   print("Tax of bike is",tax)
   print("Total price of bike is",totalprice)
   
elif price>40000 and price<=80000:
    tax=(10/100)*price
    totalprice=price+tax
    print("Tax of bike is",tax)
    print("Total price of bike is",totalprice)
    
elif price<40000 and price<=40000: 
    tax=(5/100)*price
    totalprice=tax+price
    print("Tax of bike is",tax)
    print("Total price of bike is",totalprice)