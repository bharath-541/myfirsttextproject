
#Print all prime numbers within a range
no=int(input("Enter any number:"))
for i in range(2,no):
    if no%i==0:
        print("given number is not prime number")
        break

else:
    print("given number is a prime number")
    
