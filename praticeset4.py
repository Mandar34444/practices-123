#practice set:-
#Q1. Voting Eligibility Create two variables:
#● Nationality = "Indian"
#● Age = 22
'''
nationality="Indian"
age=22
if nationality== "Indian":
    if age>=18:
        print("Eligible for voting")
    else:
        print("Not Eligible for voting")
else:
    print("Not a Indian")
'''
#Q2. Employee Job Eligibility Create variables:
#● Age = 25
#● Qualification = "Graduate" Conditions:
#● First check whether the candidate's age is greater than or equal to 21.
#● If yes, check whether qualification is Graduate.
#● If both conditions are satisfied, print "Eligible for Job".
#● Otherwise, print the appropriate message.
'''
age=25
qualification="Graduate"
if age>=21:
    if qualification=="Graduate":
        print("Eligible for the job")
    else:
        print("Not Eligible for job")
else:
    print("Not Graduate")
'''
#Q3. ATM Withdrawal Create variables:
#● Balance = 10000
#● Withdrawal Amount = 5000 Conditions:
#● First check whether the withdrawal amount is greater than zero.
#● If yes, check whether the withdrawal amount is less than or equal to the available balance.
'''
balance=10000
withdrawal_amount=5000
if balance>=0:
    if withdrawal_amount<=10000:
        print("Tansation Sucessfull")
    else:
        print("Transation Failed")
else:
    print("Insaficant Balance")
'''
#Q4. Student Admission Eligibility Create variables:
#● Marks = 75
#● Age = 19 Conditions:
#● First check whether marks are greater than or equal to 60.
#● If yes, check whether age is greater than or equal to 18.
#● If both conditions are satisfied, print "Admission Granted".
#● Otherwise, print "Admission Rejected". 
'''
marks=75
age=19
if marks>=60:
    if age>=18:
        print("Admission Granted")
    else:
        print("Admission Rejected")
else:
    print("Marks are less")
'''
#Q5. Login Verification Create variables:
#● Username = "admin"
#● Password = "admin123" Conditions:
#● First check whether the username is correct.
#● If correct, check whether the password is correct.
#● If both are correct, print "Login Successful".
#● Otherwise, print the appropriate error message
'''
username="admin"
password="admin123"
if username=="admin":
    if password=="admin123":
        print("Login successful")
    else:
        print("Login failed")
else:
    print("user name is incorect")
'''    
#Q6. Bank Loan Eligibility Create variables:
#● Salary = 45000
#● Age = 30
#Conditions:
#● First check whether salary is greater than or equal to 30000.
#● If yes, check whether age is between 21 and 60.
#● If both conditions are satisfied, print "Loan Eligible".
#● Otherwise, print "Loan Not Eligible". 
'''
salary=45000
age=30
if salary>=30000:
    if age >=21 and age<=60:
        print("Loan Eligible")
    else:
        print("Not Eligiblle for loan")
else:
    print("Your salary is minimum")
    
'''
#Create variables: ● Customer Type = "Premium"
#● Bill Amount = 5000 Conditions:
#● First check whether the customer type is Premium.
#● If yes, check whether the bill amount is greater than 3000.
#● If both conditions are satisfied, print "Eligible for Discount".
#● Otherwise, print "Not Eligible for Discount".
'''
customer_type="premium"
bill_amount=5000
if customer_type=="premium":
    if bill_amount >= 3000:
        print("Eligible for the discount")
    else:
        print("Not Eligible for the discount")
else:
    print("Not a premium")
    
'''
#Q8. Exam Result Create variables:
#● Marks = 85
#● Attendance = 80 Conditions:
#● First check whether attendance is greater than or equal to 75%.
#● If yes, check whether marks are greater than or equal to 40.
# If both conditions are satisfied, print "Pass".
# Otherwise, print the appropriate result.
'''
marks=85
attendance=80
if attendance>=75:
    if marks>=40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Your attendance is low")
'''
#Q9. Insurance Eligibility Create variables:
#● Age = 35
#● Income = 500000 Conditions:
#● First check whether age is greater than or equal to 25.
#● If yes, check whether income is greater than 300000.
#● If both conditions are satisfied, print "Eligible for Insurance". 
'''
age=35
income=500000
if age>25:
    if income>=300000:
        print("Eligible for the Insurance")
    else:
        print("Not Eligible for Insurance")
else:
    print("Yor age is less")
'''
#Q10. Product Purchase Verification Create variables:
#● Product Available = True
#● Customer Balance = 5000
#● Product Price = 3500 Conditions:
#● First check whether the product is available.
#● If available, check whether customer balance is sufficient.
#● If sufficient, print "Purchase Successful".
#● Otherwise, display an appropriate message.
'''
product_available=True
customer_balance=5000
product_price=3500
if product_available==True:
    if customer_balance>=product_price:
        print("Purchase Successful")
    else:
        print("Insufficent Balance")
else:
    print("product Not available")
'''
#Q11. Employee Information 
#Create a list containing the following employee information:
#● Employee ID = 101
#● Employee Name = "Rahul"
#● Salary = 35000
#● Experience = 2.5
#● Permanent Employee = True
#Print the complete list. 
'''
employee=[101,"Rahul",35000,2.5,True]
print(employee)
'''
#Q12. Student Information Create a list containing:
#● "Amit"
#● "Sneha"
#● "Priya"
#● "Rahul"
#● "Nikhil"
#Perform: 1. Print the complete list.
#2. Print the length of the list.
#3. Print the type of the list.
#4. Print the first and last elements.
student=["Amit","Sneha","Priya","Rahul","Nikhil"]
print(student)



    


        














        
