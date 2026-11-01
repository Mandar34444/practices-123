##Question 1: Shopping Bill Calculator
'''
laptop=int(input("Entre the price of laptop"))
mouse=int(input("Enter the price of mouse"))
key_board=int(input("Enter the price of key_board"))
bill=laptop+mouse+key_board
print(bill)
'''

##
##Write a Python program to accept the prices of 2 products from the user. Calculate and display the total amount.
##
'''
cloths=int(input("Enter the amount of cloths"))
shoes=int(input("Enter the amount of shoes"))
Total_amount=cloths+shoes
print(f'{Total_amount}')
'''
##Question 2: Employee Salary Calculator
'''
name=(input("Enter the name of employee"))
basic_salary=float(input("Enter the basic salary of employee"))
hra=basic_salary*0.20
da=basic_salary*0.10
gross_salary=basic_salary+hra+da
deduction=float(input("Enter total deduction:-"))
net_salary=gross_salary-deduction
print("\n----- Employee Salary Slip -----")
print("Employee Name:", name)
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross_salary)
print("Total Deductions:", deduction)
print("Net Salary:", net_salary)
'''
##
##Write a Python program to accept an employee's basic salary and bonus amount. Calculate and display the total salary.
'''
basic_salary=float(input("Entre the basic salary"))
bonus=float(input("Enter the bonus amount"))
total_salary=basic_salary+bonus
print(f'{total_salary}')
'''
##
##Question 3:
'''
item_name = input("Enter food item name: ")
price = float(input("Enter food item price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
gst = total * 0.05
final_bill = total + gst
print("\n----- Restaurant Bill -----")
print("Food Item:", item_name)
print("Price:", price)
print("Quantity:", quantity)
print("Total Amount:", total)
print("GST (5%):", gst)
print("Final Bill:", final_bill)
'''
##
##Write a Python program to accept the prices of 3 food items from the user. Calculate and display the total bill.
'''
item1 = float(input("Enter price of food item 1: "))
item2 = float(input("Enter price of food item 2: "))
item3 = float(input("Enter price of food item 3: "))
total_bill = item1 + item2 + item3
print("Total Bill:", total_bill)
'''
##
##Question 4: Student Marks Calculator
'''
name=(input("Enter the student name"))
history=float(input("Enter the history marks"))
science=float(input("Enter the science marks"))
maths=float(input("Enter the maths marks"))
total_marks=history+science+maths
avarge_marks=total_marks/3
print("\n------Stsudent Marksheet--------")
print(f'{total_marks}')
print(f'{avarge_marks}')
'''
##
##Write a Python program to accept marks of 3 subjects. Calculate and display the total marks and average marks.
'''
mark1 = float(input("Enter marks of subject 1: "))
mark2 = float(input("Enter marks of subject 2: "))
mark3 = float(input("Enter marks of subject 3: "))
total = mark1 + mark2 + mark3
average = total / 3
print("Total Marks:", total)
print("Average Marks:", average)
'''
##
##Question 5: Online Shopping Calculator
'''
item1 = float(input("Enter price of item 1: ₹"))
item2 = float(input("Enter price of item 2: ₹"))
item3 = float(input("Enter price of item 3: ₹"))

total = item1 + item2 + item3

discount = total * 0.10
final_amount = total - discount

print("\n----- Shopping Bill -----")
print("Total Amount: ₹", total)
print("Discount (10%): ₹", discount)
print("Final Amount: ₹", final_amount)
'''
##
##Write a Python program to accept the price and quantity of a product. Calculate and display the total price.
'''
price = float(input("Enter the price of the product: ₹"))
quantity = int(input("Enter the quantity: "))

total_price = price * quantity

print("Total Price: ₹", total_price)
'''
##
##Question 6: Electricity Bill Calculator
'''
units = int(input("Enter electricity units consumed: "))
rate = float(input("Enter price per unit: "))
bill = units * rate
print("Total Electricity Bill =", bill)
'''

##
##Write a Python program to accept electricity units consumed and the rate per unit. Calculate and display the total electricity charge.
'''
units = int(input("Enter electricity units consumed: "))
rate = float(input("Enter rate per unit: "))
total_charge = units * rate
print("Total Electricity Charge =", total_charge)
'''
##
##Question 7: Hotel Bill Calculator
##
##Write a Python program to accept room rent per day and the number of days stayed. Calculate and display the total room rent.
'''
rent = float(input("Enter room rent per day: "))
days = int(input("Enter number of days stayed: "))
total_rent = rent * days
print("Total Room Rent =", total_rent)
'''
##Question 8: Fuel Expense Calculator
##
##Write a Python program to accept the number of petrol litres purchased and the price per litre. Calculate and display the total petrol cost.
##
'''
litres = float(input("Enter petrol litres purchased: "))
price = float(input("Enter price per litre: "))
total_cost = litres * price
print("Total Petrol Cost =", total_cost)
'''
##Question 9: Mobile Recharge Calculator
##
##Write a Python program to accept a mobile recharge amount and a service fee. Calculate and display the final amount.
'''
recharge = float(input("Enter mobile recharge amount: "))
fee = float(input("Enter service fee: "))

final_amount = recharge + fee

print("Final Amount =", final_amount)
'''
##
##Question 10: Simple Interest Calculator
##
##Write a Python program to accept the principal amount, rate of interest, and time in years. Calculate and display the simple interest.
##
'''
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)

'''
##Question 11: Rectangle Calculator
##
##Write a Python program to accept the length and width of a rectangle. Calculate and display its area.
##
'''
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width

print("Area of Rectangle =", area)
'''


##Question 12: Square Calculator
##
##Write a Python program to accept the side of a square. Calculate and display its area.
##
'''
side = float(input("Enter the side of the square: "))

area = side * side

print("Area of Square =", area)
'''
##Question 13: Age Calculator
##
##Write a Python program to accept a person's birth year and the current year. Calculate and display the person's age.
##
'''
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))

age = current_year - birth_year

print("Your age is:", age, "years")
'''
##Question 14: Discount Calculator
##
##Write a Python program to accept a product price and discount amount. Calculate and display the final price after discount.
##
'''
price = float(input("Enter product price: "))
discount = float(input("Enter discount amount: "))

final_price = price - discount

print("Final Price After Discount =", final_price)
'''
##Question 15: GST Calculator
##
##Write a Python program to accept a product price. Calculate 18% GST and display the GST amount and final price.
##
'''
price = float(input("Enter product price: "))

gst = price * 18 / 100
final_price = price + gst

print("GST Amount =", gst)
print("Final Price =", final_price)
'''

##Question 16: Distance Calculator
##
##Write a Python program to accept speed and time. Calculate and display the distance travelled.
##
'''
speed = float(input("Enter speed: "))
time = float(input("Enter time: "))

distance = speed * time

print("Distance Travelled =", distance)
'''

##Question 17: Temperature Converter
##
##Write a Python program to accept temperature in Celsius. Convert it into Fahrenheit and display the result.
##
'''
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)
'''

##Question 18: Daily Wage Calculator
##
'''
daily_wages = float(input("Enter daily wages: "))
working_days = int(input("Enter number of working days: "))

total_salary = daily_wages * working_days

print("Total Salary =", total_salary)
'''

##Write a Python program to accept daily wages and the number of working days. Calculate and display the total salary.
##
##Question 19: Percentage Calculator
##
##Write a Python program to accept total marks obtained and maximum marks. Calculate and display the percentage.
##
'''
total_marks = float(input("Enter total marks obtained: "))
maximum_marks = float(input("Enter maximum marks: "))

percentage = (total_marks / maximum_marks) * 100

print("Percentage =", percentage, "%")
'''
##Question 20: Profit Calculator
##
##Write a Python program to accept the cost price and selling price of a product. Calculate and display the profit amount.
'''
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

profit = selling_price - cost_price

print("Profit Amount =", profit)
'''
