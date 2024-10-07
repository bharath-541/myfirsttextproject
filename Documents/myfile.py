
#Print multiplication table of a given number (1 x 1 = 1 …)
pint=int(input("Enter any number for which you want to generate table:"))
for i in range(1,11):
    vo=pint*i
    print(pint,"x",i,"=",vo)

#Count the total number of digits in a number
num=(input("Enter any number:"))
c=0
for i in num:
    c+=1
print(c)


#write a list in reverse order
L1=["apple","mango","cherry","banana"]
n=len(L1)
for j in range(1,(n+1)):
    print(L1[-j],end=' ')
    

#Print all prime numbers within a range
no=int(input("Enter any number:"))
for i in range(2,no):
    if no%i==0:
        print("given number is not prime number")
        break

else:
    print("given number is a prime number")



#Display Fibonacci series up to 10 terms
n=int(input("#Display Fibonacci series up to 10 terms"))
m=[0,1]
if n<=0:
    print("please enter positive value")
else:
    for i in range(1,n):
        m.append(m[-2]+m[-1])
print(m)



#Display Fibonacci series up to 10 terms
o=int(input("Display Fibonacci series up to 10 terms:"))
m=0
n=1
print(0,end=" ")
for i in range(1,o):
    j=m+n
    m=n
    n=j
    print(m,end=" ")


   
#Reverse a integer number without using any built-in function
v=int(input("Enter any integer:"))
m=str(v)
print(m[-1::-1])


 
#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#The sum of all evens is 2550. And the sum of all odds is 2500.
v=0
m=0
for i in range(0,101):
    if i%2==0:
        v+=i
    else:
        m+=i
print("The sum of all the even numbers is:",v)
print("The sum of all the odd numbers is:",m)



#Write a Python program that accepts a string and calculates the number of digits and letters.
inf=input("Enter any word with letters and numbers:")
counti=0
countc=0
for i in inf:
    if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
        counti+=1
    else:
        countc+=1
print(counti)
print(countc)


#Write a Python program to print the pattern using a loop.

for i in range(1,6):
    for j in range(6-i,0,-1):
        print(j,end=" ")
    print()
for i in range(1,6):
    if i<=5:
        for j in range(1,(i+1)):
            print("*",end=" ")
    print()
for l in range(1,5):
    for v in range(6-l,1,-1):
        print("*",end=" ")

    print()



        
   
  




        












                    

    








    













      
