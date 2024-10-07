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
