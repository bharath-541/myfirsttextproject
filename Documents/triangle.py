side1=int(input("Enter length of 1st side of the triangle:"))
side2=int(input("Enter length of 2nd side of the triangle:"))
side3=int(input("Enter length of 3rd side of the triangle:"))
if side1==side2 and side2==side3 and side3==side1:
    print("Given triangle is equilateral triangle")
elif side1!=side2 and side2!=side3 and side3!=side1:
    print("Given triangle is scalene traingle")
else:
    print("Given triangle is isosceles triangle")
