unit=int(input("Enter no of units consumed:"))
if unit<=100:
    print("your bill is exempted from billing")
elif unit>100 and unit<=200:
    print("your bill is",(unit-100)*5)
elif unit>200:
    print("your bill is",500+((unit-200)*10))


