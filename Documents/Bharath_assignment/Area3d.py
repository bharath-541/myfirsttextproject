'''
Write a program to calculate AREA & Volume of 3D mathematical ShapesWrite a program to calculate AREA &
Volume of 3D mathematical Shapes (Sphere, Cube, Cuboid, Cone)
'''
R=int(input("Enter the radius of the sphere:"))
C_1=int(input("Enter the length of the side of the cube:"))
L1=int(input("Enter the length of the of the cuboid:"))
W1=int(input("Enter the width of the of the cuboid:"))
H1=int(input("Enter the heigth of the of the cuboid:"))
CH1=int(input("Enter the height of the of the cone:"))
CR1=int(input("Enter the radius of the of the cone:"))
pie=3.14
print("The surface area of the sphere is:",(4*pie)*(R**2))
print("The volume of the sphere is:",(R**3)*pie*(4/3))
print("The surface area of the cube is:",6*(C_1**2))
print("The volume of the cube is:",C_1**3)
print("The surface area of the Cuboid is:",2*((L1*W1)+(W1*H1)+(H1*L1)))
print("The volume of the cuboid is:",L1*W1*H1)
CL1=((CH1**2)+(CR1**2))**0.5
print("The surface area of the cone is:",(pie*CR1)*(CR1+CL1))
print("The volume of the cone is:",pie*(CR1**2)*(CH1)*(1/3))
      


