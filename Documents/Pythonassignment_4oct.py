# 1 write a program to check whether a year is leap year or not
year=int(input("Enter any year:"))
if year%4==0:
    print("Given year is a leap year")
else:
    print("Given year is not leap year")


# 2 Write a program to check whether a number entered is three digit number or not
number=int(input("Enter any number:"))
if number>99 and number<1000:
    print("Given number is three digit number")
else:
    print("Given number is not three didgit number")


# 3 Write a program to check whether a person is eligible for voting
#  or not.(voting age>=18)
age=int(input("Enter your age:"))
if age>=18:
    print("You are elgible to vote")
else:
    print("you are not elgible to vote")


# 4 Write a program to check whether the last digit of
# a number( entered by user ) is 3.
num=int(input("Enter any number:"))
count=str(num)
if count[-1]=="3":
    print("last digit of the given number is three")
else:
    print("last digit of the given number is not three")


# 5 Write a Python program to check whether an alphabet is a vowel or consonant
letter=input("Enter any alphabet:")
if letter=="a" or letter=="A" or letter=="e" or letter=="E" or letter=="i" or letter=="I"  or letter=="o" or letter=="O" or letter=="u" or letter=="U":
    print("Given letter is Vowel")
else:
    print("Given letter is consonant")


# 6 Write a Python program to convert a month name to a number of days
month=(input("Enter the name of the month:"))
if month=="January" or month=="january" or month=="March" or month=="march" or month=="may" or month=="May" or month=="July" or month=="july" or month=="August" or month=="august" or  month=="october" or month=="October" or month=="December" or month=="december":
          print("Given month has 31 Days")
elif month=="febrauary" or month=="Febrauary":
    print("given month has 28 days")
else:
    print("Given month has 30 days")


# 7 Write a Python program to check if a triangle is equilateral,
#    isosceles or scalene
side1=int(input("Enter length of 1st side of the triangle:"))
side2=int(input("Enter length of 2nd side of the triangle:"))
side3=int(input("Enter length of 3rd side of the triangle:"))
if side1==side2 and side2==side3 and side3==side1:
    print("Given triangle is equilateral triangle")
elif side1!=side2 and side2!=side3 and side3!=side1:
    print("Given triangle is scalene traingle")
else:
    print("Given triangle is isosceles triangle")


'''
 8 Write a program to calculate the electricity bill (accept number of unit from user)
according to the following criteria :
Unit Price
First 100 units no charge
Next 100 units Rs 5 per unit
After 200 units Rs 10 per unit
'''
unit=int(input("Enter no of units consumed:"))
if unit<=100:
    print("your bill is exempted from billing")
elif unit>100 and unit<=200:
    print("your bill is",(unit-100)*5)
elif unit>200:
    print("your bill is",500+((unit-200)*10))


'''
 9 Write a program to accept the cost price of a bike and display the road tax to be
paid according to the following criteria :
Cost price (in Rs) Tax
> 100000 15 %
> 50000 and <= 100000 10%
<= 50000 5%
'''
cost=int(input("Enter the price of the bike:"))
if cost<=50000:
    print("Road tax of the bike is",(5/100)*(cost))
elif cost>50000 and cost<=100000:
    print("Road tax of the bike is",(cost)*(10/100))
elif cost>100000:
    print("Road tax of the bike is",(cost)*(15/100))


'''
 10 Accept the marked price from the user and calculate the Net amount as(Marked
Price – Marked Price Discount) to pay according to following criteria:
Discount
>10000 20%
>7000 and <=10000 15%
<=7000 10%
'''
mprice=int(input("Enter your marked price:"))
if mprice<=7000:
    print("Your net amount is :",mprice-(mprice*(10/100)))
elif mprice>7000 and mprice<=10000:
    print("Your net amount is :",mprice-(mprice*(15/100)))
else:
    print("Your net amount is :",mprice-(mprice*(20/100)))

    











