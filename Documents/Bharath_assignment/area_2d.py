#Write a program to calculate AREA & Perimeter of 2D mathematical Shapes (Circle, Square, Rectangle, Triangle)
R=int(input("Enter radius of the Circle: "))
S_1=int(input("Enter length of the side of the Square: "))
L_1=int(input("Enter length of the rectangle: "))
B_1=int(input("Enter breadth of the rectangle: "))
TS_1=int(input("Enter length of 1st side of the triangle: "))
TS_2=int(input("Enter length of 2st side of the triangle: "))
TS_3=int(input("Enter length of 3rd side of the triangle: "))
pie=3.14
area_circle=(pie)*(R**2)
print("The area of the circle is:",area_circle)
print("The perimeter of the cicrcle is:",2*pie*R)
print("The area of the square is:",S_1**2)
print("The perimeter of the Square is:",4*S_1)
print("The area of the rectangle is:",L_1*B_1)
print("The perimeter of the rectangle is:",2*(L_1+B_1))
sp=(TS_1+TS_2+TS_3)/2

tarea=(sp*(sp-TS_1)*(sp-TS_2)*(sp-TS_3))**0.5

print("The area of the triangle is:",tarea)
print("The perimeter of the traingle is:",TS_1+TS_2+TS_3)
