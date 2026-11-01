'''
units=int(input("Enter the number of units"))
print(units*7.5)
'''
#2
'''
l=int(input("Enter the length"))
b=int(input("Enter the breadth"))
area=l*b
perimeter=(l+b)*2
print(f'{area=}')
print(f'{perimeter=}')
'''

#3
'''
sem1=float(input("Enter the marks of semester1"))
sem2=float(input("Enter the marks of semester 2"))

total_marks=sem1+sem2
average=total_marks/2

print("Total_marks",total_marks)
print("Average of marks",average)

'''
#4W.A.P a python program that the user to input
#the priciple amount,rate of intrest,&time in years calculate the simple intrest using formula
#SI=(p*r*t)/100
'''
principal_amount=int(input("Enter your amount"))
rate_ofinterst=float(input("Enter the rate of interst"))
time_inyears=int(input("Enter the no of years"))
SI=(principal_amount*rate_ofinterst*time_inyears)/100
print("Simple intrest",SI)
'''
#5 W.A.P a python program to get prices of 5 products
# From user&Print 50% discount_price of products.
'''
wheat=int(input("Enter the price of wheat:-"))
rice=int(input("Enter the price of rice:-"))
dryfruits=int(input("Enter the price of dryfruits:-"))
jawar=int(input("Enter the price of jawar:-"))
Bajra=int(input("Enter the price of Bajra:-"))
total_price=wheat+rice+dryfruits+jawar+Bajra
disc_price=total_price/2
print("total price",total_price)
print("disc price",disc_price)
'''
#6 write a python program that asks the user to input the princple
#amount,rate of intrest &time in years,calculate the EMI.
'''
princple_amount=int(input("Enter your amount"))
rate_ofintrest=float(input("Enter your rate of intrest"))
time_inyears=int(input("Enter your time of years"))
SimpleIntrest=(princple_amount*rate_ofintrest*time_inyears)/100
EMI=(princple_amount+SimpleIntrest)/(time_inyears*12)
print(SimpleIntrest)
print(EMI)
'''

