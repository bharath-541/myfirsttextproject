cost=int(input("Enter the price of the bike:"))
if cost<=50000:
    print("Road tax of the bike is",(5/100)*(cost))
elif cost>50000 and cost<=100000:
    print("Road tax of the bike is",(cost)*(10/100))
elif cost>100000:
    print("Road tax of the bike is",(cost)*(15/100))
    
