##Task Questions – Python Arithmetic Practice
##1) Create a variable to store an integer value and print it.
'''
age=26
print(age)
'''
##2) Create a variable to store a float value and print it.
'''
cgpa=float(input("Enter your cgpa"))
print(cgpa)
'''
##3) Create a variable to store a string (your name) and print it.
'''
name=(input("your name:-"))
print(name)
'''
##4) Create a variable is_student and assign a boolean value (True or False). Print it
'''
is_student=True
print(is_student)
'''
##5) Create four variables of type int, float, string, and boolean and print each variable along with its datatype using type()
'''
marks=80
cgpa=80.9
name="Mandar"
is_fail=False
print(marks)
print(cgpa)
print(name)
print(is_fail)
'''
##6) Create two numbers and print the result of floor division (//).
'''
a=int(input("Entre the value of a"))
b=int(input("Enter the value of b"))
ans=a//b
print(ans)
'''
##7) Create two numbers and print the result of exponentiation (**).
'''
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
ans=a**b
print(ans)
'''
##8) Create two numbers and print the result of all arithmetic operations (+ , - , * , / , // , % , **).
'''
f=int(input("Enter the value of f"))
n=int(input("Enter the value of n"))
print(f+n)
print(f-n)
print(f*n)
print(f/n)
print(f//n)
print(f%n)
print(f**n)
'''

##9) Create three numbers and print their total sum.
'''
s=int(input("Enter the value of s"))
q=int(input("Enter the value of q"))
r=int(input("Enter the value of r"))
sum=s+q+r
print(sum)
'''
##10) Create two numbers and print the difference between them.
'''
T=int(input("Enter the value of T"))
Y=int(input("Enter the value of t"))
difference=T-Y
print(difference)
'''

##11) Create two numbers and print their average.
'''
u=int(input("Enter your number"))
v=int(input("Enter your number"))
sum=u+v
avg=sum/2
print(sum)
print(avg)
'''

##12) Create one number and print its square.
'''
A=int(input("Enter your number"))
square=A*A
print(square)
'''

##13) Create one number and print its cube.
'''
B=int(input("Enter the value of B"))
cube=B*B*B
print(cube)
'''
##14) Write a Python program to calculate Simple Interest.[ Formula: SI = (P × R × T) / 100 ]
'''
priciple_ofAmount=int(input("Enter the value"))
rate_Ofinterest=float(input("Enter the value"))
times_Inyears=int(input("Enter the value"))
SI=(priciple_ofAmount*rate_Ofinterest*times_Inyears)
print(SI)
'''
##15) Write a Python program to calculate the Area of a Rectangle. [ Formula: Area = length × width ]
'''
length=int(input("Enter the length"))
width=int(input("Enter the width"))
Area=length*width
print(Area)
'''
##16) Write a Python program to calculate the Perimeter of a Rectangle.[Formula: Perimeter = 2 × (length + width)]
'''
length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = 2 * (length + width)
print("Perimeter of Rectangle =", perimeter)
'''
##17) Write a Python program to calculate the Area of a Square. [ Formula: Area = side × side ]
'''
side=float(input("Enter the side"))
Area=side*side
print(Area)
'''
##18) Write a Python program to calculate the Average of three numbers. [ Formula: (a + b + c) / 3 ]
'''
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))
average=a+b+c/3
print(average)
'''
