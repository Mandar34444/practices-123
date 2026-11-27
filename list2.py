#list 2:
#1. Create a list named students containing: "Aarav", "Kartik", "Riya", "Kabir", "Meera", "Kartik", "Anaya", "Kabir". Display the complete list.
'''
student=["Aarav", "Kartik", "Riya", "Kabir", "Meera", "Kartik", "Anaya", "Kabir"]
print(student)
'''
#2. Check whether "Kartik" is present in the students list using the in operator. Display the result.
'''
student=["Aarav", "Kartik", "Riya", "Kabir", "Meera", "Kartik", "Anaya", "Kabir"]
print("Kartik" in student)
'''
#3. Check whether "Pranav" is present in the students list. Display the result.
'''
student=["Aarav", "Kartik", "Riya", "Kabir", "Meera", "Kartik", "Anaya", "Kabir"]
print("Pranav"in student)
'''
#4. Find how many times "Kabir" appears in the students list using count().
'''
student=["Aarav", "Kartik", "Riya", "Kabir", "Meera", "Kartik", "Anaya", "Kabir"]
print(student.count("Kabir"))
'''
#5. Find and display the index position of "Meera" in the students list using index().
'''
student=["Aarav", "Kartik", "Riya", "Kabir", "Meera", "Kartik", "Anaya", "Kabir"]
print(student.index("Meera"))
'''
#6. Create a list named products containing "Laptop", "Mouse", "Keyboard", "Monitor", "Mouse", "Printer", "Mouse". Find the count of "Mouse" and its first index position.
'''
prouducts=["Laptop", "Mouse", "Keyboard", "Monitor", "Mouse", "Printer", "Mouse"]
print(prouducts.count("Mouse")
'''
#7. Create a list of cities: "Pune", "Mumbai", "Nashik", "Nagpur", "Kolhapur". Check whether "Pune" and "Delhi" are present.
'''
cities=["Pune", "Mumbai", "Nashik", "Nagpur", "Kolhapur"]
print("Delhi"in cities)
print("Pune"in cities)
'''
#8. Create marks containing 76, 92, 65, 88, 71, 95, and 80. Display the values in ascending order using sorted(), without changing the original list.
'''
marks=[76, 92, 65, 88, 71, 95,80]
print(sorted(marks))
'''
#9. Using the same marks list, display the values in descending order using sorted().
'''
marks=[76, 92, 65, 88, 71, 95,80]
marks.sort(reverse =True)
print(marks)
'''
#10. Create prices containing 450, 120, 999, 275, 650, and 310. Sort it in ascending order using sort() and display the updated list.
'''
prices=[450, 120, 999, 275, 650,310]
prices.sort()
print(prices)
'''
#11. Using the prices list, sort the values in descending order using sort() with an appropriate argument.
'''
prices=[450, 120, 999, 275, 650,310]
prices.sort(reverse=True)
print(prices)
'''
#12. Create names containing "Kavya", "Aarav", "Meera", "Kabir", and "Riya". Display the names alphabetically using sorted(). Then reverse the original list using reverse() and display it.
'''
names=["Kavya", "Aarav", "Meera", "Kabir","Riya"]
names.sort()
print(names)
names.sort(reverse=True)
print(names)
'''
#13. Create sales containing 1250, 1800, 950, 2200, 1600, and 1450. Find and display the maximum, minimum, and sum of all values.
'''
sales=[1250, 1800, 950, 2200, 1600,1450]
print(sum(sales))
'''
#14. Using the sales list, calculate and display the average sales value using sum() and len().
'''
sales=[1250, 1800, 950, 2200, 1600,1450]
print(sum(sales)/len(sales))
'''
#15. Create expenses containing 3500, 4200, 2800, 5100, 3900, and 4500. Display the number of elements, total, highest, lowest, and average expense.
'''
expenses= [3500, 4200, 2800, 5100, 3900,4500]
print(len(expenses))
print(min(expenses))
print(max(expenses))
'''
#Given student_marks = [78, 92, 65, 88, 92, 74, 81, 65, 95], find the highest and lowest marks, total and average marks, count how many times 92 appears, check whether 85 is present, and display the marks in Page 1 Python | List Searching and Operationsascending and descending order.
'''
student_marks = [78, 92, 65, 88, 92, 74, 81, 65, 95]
print(max(student_marks))
print(min(student_marks))
print(sum(student_marks))
print(sum(student_marks)/len(student_marks))
print(student_marks.count(92))
print(85 in student_marks)
student_marks.sort()
print(student_marks)
student_marks.sort(reverse=True)
print(student_marks)

'''






















