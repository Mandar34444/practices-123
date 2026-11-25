#For Loop:
# Q1. Write a Python program to print all numbers from 1 to 50 using a for loop.
'''
for i in range(1,51):
    print(i)
'''
#Q2. Write a Python program to print all numbers from 50 to 1 in descending order.
'''
for i in range(51,1,-1):
    print(i)
'''
#Q3. Write a Python program to print all numbers between 100 and 200 that are divisible by 5.
'''
for i in range(100,201):
     if i%5==0:
        print(i)
'''
#Q4. Write a Python program to print all odd numbers between 50 and 150.
'''
for i in range(50,151):
    if i%2!=0:
        print(i)
'''
#Q5. Write a Python program to print all even numbers between 1 and 200.
'''
for i in range(1,201):
    if i % 2 ==0:
        print(i)
'''
#Q6. Write a Python program to print numbers from 10 to 100 with an increment of 5.
'''
for i in range(10,101,5):
    print(i)
'''
#Q7. Write a Python program to print numbers from 200 to 100 with a decrement of 10. 
'''
for i in range(200,100,-10):
       print(i)
'''
#Q8. Write a Python program to print all numbers between 1 and 200 that are divisible by both 3 and 5.
'''
for i in range(1,201):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
'''
#Q9. Write a Python program to print all numbers between 1 and 150 that are divisible by 7 but not divisible by 2. 
'''
for i in range(1,151):
    if i % 7 == 0 and i % 2 != 0:
        print(i)
'''
#   Q10. Write a Python program to print all numbers between 1 and 100 that are divisible by either 4 or 6.
'''
for i in range(1,101):
    if i % 4 == 0 or i % 6 == 0:
        print(i)
'''
#Q11. Write a Python program to print all numbers between 1 and 300 that are divisible by 3, 5, and 10.
'''
for i in range(1,301):
    if i % 3 == 0 and i % 5 == 0 and i % 10 == 0:
        print(i)
'''        
#Q12. Write a Python program to print all numbers between 50 and 200 that are not divisible by 3.
'''
for i in range(50,201):
    if i % 3 != 0:
        print(i)
'''
#Q13. Write a Python program to print numbers from 1 to 100 and display whether each number is even or odd.
'''
for i in range(1,101):
    if i % 2 == 0:
        print(i,"Even Number")
    else:
        print(i,"odd Number")
'''
#Q14. Write a Python program to print numbers from 1 to 100 and display:
#● "Divisible by 3" if the number is divisible by 3
#● "Divisible by 5" if the number is divisible by 5.
#● "Divisible by both" if divisible by both 3 and 5.
#● "Not divisible" otherwise.
'''
for i in range(1,101):
    if i % 3 == 0:
        print(i,"Divisible by 3")
    elif i % 5 == 0:
        print(i,"Divisible by 5")
    elif i % 3 == 0 or i % 5:
        print(i,"Divisible by both")
    else:
        print(i,"Not Divisible")
'''
#Q15. Write a Python program to print numbers from 1 to 100 and identify whether each number is:
#● Even and divisible by 4.
#● Odd and divisible by 3.
#● Neither of the above. 
'''
for i in range(1,101):
    if i % 2 == 0 and i % 4 == 0:
        print(i,"Even & divisible by 4")
    elif i % 2 !=0 and i % 3 == 0:
        print(i,"Odd and divisible by 3")
        
    else:
        print(i,"Neither of the above")
'''
#Q16. Write a Python program to print numbers from 1 to 150. Display "Small" for numbers below 50, "Medium" for numbers between 50 and 100, and "Large" for numbers above 100.
'''
for i in range(1,151):
    if i < 50:
        print(i,"Small")
    elif i<=100:
        print(i,"Medium")
    elif i>100:
        print(i,"Large")
'''
#Q17. Write a Python program to print numbers from 1 to 100. Display:
   #● "Multiple of 2" for numbers divisible by 2.
    #● "Multiple of 3" for numbers divisible by 3.
    #● "Multiple of both 2 and 3" for numbers divisible by both.
    #● "Other" for remaining numbers.

'''
for i in range(1, 101):

    if i % 2 == 0 and i % 3 == 0:
        print(i, "- Multiple of both 2 and 3")

    elif i % 2 == 0:
        print(i, "- Multiple of 2")

    elif i % 3 == 0:
        print(i, "- Multiple of 3")

    else:
       print(i, "- Other")
'''
#Q18. Write a Python program to calculate the sum of all numbers from 1 to 100 using a while loop.
'''
total = 0

for i in range(1, 101):
    total = total + i

print("Sum of numbers from 1 to 100 is:", total)
'''

#Q19. Write a Python program to calculate the sum of all even numbers between 1 and 100.
'''
total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total = total + i

print("Sum of even numbers:", total)
'''
#Q20. Write a Python program to calculate the sum of all odd numbers between 1 and 100. 
'''
total = 0

for i in range(1, 101):
    if i % 2 != 0:
        total = total + i

print("Sum of odd numbers:", total)     
'''
#Q21. Write a Python program to count how many numbers between 1 and 200 are divisible by 7.
'''
count = 0

for i in range(1, 201):
    if i % 7 == 0:
        count = count + 1

print("Total numbers divisible by 7:", count)
'''
#Q22. Write a Python program to count how many even and odd numbers are present between 1 and 100. 
'''
even_count = 0
odd_count = 0

for i in range(1, 101):

    if i % 2 == 0:
        even_count = even_count + 1

    else:
        odd_count = odd_count + 1

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)
'''
#Q23. Write a Python program to calculate the sum of all numbers between 1 and 100 that are divisible by both 3 and 7.
'''
total = 0

for i in range(1, 101):

    if i % 3 == 0 and i % 7 == 0:
        total = total + i

print("Sum of numbers divisible by both 3 and 7:", total)
'''
#Q24. Write a Python program to print the multiplication table of 7 using a for loop (7 × 1 to 7 × 10). 
'''
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)
'''
#Q25. Write a Python program to print the following pattern using a for loop: 
'''
for i in range(1, 11):
    for j in range(1, i + 1):
        print(j, end="")
    print()
''' 
#Q26. Write a Python program to print all numbers between 1 and 500 whose last digit is 5.
'''
for i in range(1, 501):
    if i % 10 == 5:
        print(i)
'''

#Q27. Write a Python program to find and print all numbers between 1 and 100 that are divisible by 2, 3, and 5 simultaneously.
'''
for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        print(i)
'''
#Q28. Write a Python program to calculate the product of all numbers from 1 to 10 using a while loop. 
'''
product = 1

for i in range(1, 11):
    product = product * i

print("Product:", product)
'''
#Q29. Write a Python program to print all numbers between 1 and 100 in which the number is divisible by 2 or 5, but not both.
'''
for i in range(1, 101):
    if (i % 2 == 0 and i % 5 != 0) or (i % 2 != 0 and i % 5 == 0):
        print(i)
'''
#Q30. Write a Python program to count the total number of numbers between 1 and 500 that are:
#    ● Divisible by 3.
#    ● Divisible by 5.
#● Divisible by both 3 and 5.
'''
count_3 = 0
count_5 = 0
count_both = 0

for i in range(1, 501):
    if i % 3 == 0:
        count_3 += 1

    if i % 5 == 0:
        count_5 += 1

    if i % 3 == 0 and i % 5 == 0:
        count_both += 1

print("Divisible by 3:", count_3)
print("Divisible by 5:", count_5)
print("Divisible by both 3 and 5:", count_both) 
'''


    

