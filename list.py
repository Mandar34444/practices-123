#List:-
#1. Create a list named students containing the names of seven students. Print the complete list.
'''
stu=["karan","kunal","kartik","kumar","krupa","kiayara","kedar"]
print(stu)
'''
#2. Create a list named sales containing these values: 1200, 2500, 1800, 3200, 2750, 4100. Print the third and fifth elements using their index positions.
'''
sales=[1200,2500,1800,3200,2750,4100]
print(sales[3])
print(sales[5])
'''
#3. Create a list of six city names. Display the first three cities and then display the last three cities using slicing.
'''
cities=["pune","nashik","nagpur","mumbai","yavatmal","vashim"]
print(cities[0:3])
print(cities[-4:-1])
'''
#4. Create a list containing different data types: an integer, a decimal value, a Boolean value, and a string. Print the list.
'''
data_types=[100,30.33,True,"Adyayan"]
print(data_types)
'''
#5. Create a list of eight numbers. Print all elements one by one using a for loop.
'''
num=[112,334,56,657,797,85,86,90]
for i in num:
    print(i)
'''
#6. Create a list of marks for six students. Use a loop to print only the even-numbered marks.
'''
marks=[98,77,86,45,67,87]
for i in marks:
    if i % 2==0:
        print(i)
'''
#7. Create a list of five employee names. Change the name stored at index position 2 to a new employee name and print the updated lis
'''
employee=["kavya","kavita","kaveri","kirti","krupa"]
employee[2]="kiayara"
print(employee)
'''
#8. Create a list named courses containing Python, SQL, Excel, and Power BI. Add Tableau at the end using append().
'''
courses=["python","sql","exel","power BI"]
courses.append("tableau")
print(courses)
'''
#9. Create a list of five product names. Insert a new product at index position 2 using insert().
'''
product=["laptop","mouse","keybord","charger","camera"]
product.insert(2,"P.C")
print(product)
'''
#10. Create a list named departments containing HR, Sales, and IT. Add the values Finance and Marketing together at the end using extend().
'''
deparment=["HR","Sales","IT"]
deparment.extend(["Finance","Marketing"])
print(deparment)
'''
#11. Create a list of numbers from 10 to 50 (use at least six values). Add one new number at the end, then insert another number at index position 3. Print the final list
'''
numbers=[10,20,30,40,50]
numbers.append(90)
print(numbers)
numbers.insert(3,100)
print(numbers)
'''
#12. Create a list of seven student names. Remove the name “Karan” from the list using remove() and print the updated list.
'''
stu=["kartik","kedar,""kamlesh","karan","kumar","rohit","tushar"]
stu.remove("karan")
print(stu)
'''
#13. Create a list of eight numbers. Remove the element at index position 4 using pop() and print the updated list.
'''
numbers=[12,25,67,87,86,89,65,56]
numbers.pop(4)
print(numbers)
'''
#14. Create a list of five subject names. Use clear() to remove all elements and print the list after clearing it.
'''
subject=["science","english","marathi","hindi","maths"]
subject.clear()
print(subject)
'''
#15. Create a list of six grocery items. Remove one item by its value and another item by its index position. Display the final list.
'''
grocery=["wheat","moog","jawar","bajra","fruits","vegitables"]
grocery.remove("moog")
print(grocery)
grocery.pop(4)
print(grocery)
'''
#16. Create a list of ten numbers. Use a for loop to print only the numbers greater than 25.
'''
numbers=[30,13,43,23,64,67,678,67,33,11]
for i in numbers:
   if i>=25:
        print(i)
'''
#17. Create a list of student names. Print the name at index 3, print elements from index 1 to 4 using slicing, and then print the complete list using a loop.
'''
students=["viraj","kiran","mohit","arjun","vikas","parjoyt"]
print(students[3])
print(students[1:4])
for i in students:
    print(i)
'''
#18. Create a list of marks: [45, 78, 62, 91, 55, 84]. Print all marks using a loop. Then add 70 using append(), insert 88 at index 2, and print the updated list.
'''
marks=[45, 78, 62, 91, 55, 84]
for i in marks:
    print(i)
marks.append(70)
print(marks)
marks.insert(2,88)
print(marks)
'''
#19. Create a list of five technology names. Extend the list with three more technology names. Remove one specified technology using remove(), then print the final list.
'''
technology = ["Python", "Java", "JavaScript", "C++", "C#"]
technology.extend(["c","react"])
print(technology)
technology.remove("c")
print(technology)
'''

#20. Create a list of six employee names. Update one name, append a new name, insert another name at index 1, and remove one name by value. Print the list after each operation.
'''
employees = ["Rahul", "Amit", "Priya", "Sneha", "Rohan", "Neha"]

print("Original List:", employees)


employees[2] = "Pooja"
print("After Update:", employees)


employees.append("Karan")
print("After Append:", employees)


employees.insert(1, "Akash")
print("After Insert:", employees)


employees.remove("Sneha")
print("After Remove:", employees)

'''
        



    
