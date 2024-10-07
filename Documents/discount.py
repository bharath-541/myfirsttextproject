mprice=int(input("Enter your marked price:"))
if mprice<=7000:
    print("Your net amount is :",mprice-(mprice*(10/100)))
elif mprice>7000 and mprice<=10000:
    print("Your net amount is :",mprice-(mprice*(15/100)))
else:
    print("Your net amount is :",mprice-(mprice*(20/100)))
    
