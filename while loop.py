# While loop
# Example no 1
'''
count=1

while count<=100:
    print(count)
    count+=1
'''
#Example no 2
'''
count2=1
while count2<100:
    print(count2)
    count2+=2
'''
#Example no 3
'''
count3=0
while count3<100:
    if count3%2==0:
        print(count3,"even number")
    else:
        print(count3,"odd number")
    count3+=1
'''
#Example no 4
'''
count4=1
while count4<100:
    if count4%3==0 and count4%7==0:
        print(count4)
    count4+=1
'''
#Example no 5
'''
count5=1
while count5<=50:
    print(count5)
    count5+=1
'''
#Example no 6
'''
count6=50
while count6>1:
    print(count6)
    count6-=1
'''
#Example no 7
'''
count7=100
while count7<=200:
    if count7%5==0:
        print(count7)
    count7+=1
'''
#Write a Python program to print all odd numbers between 50 and 150.
'''
count8=50
while count8<=150:
    if count8%2!=0:
        print(count8)
    count8+=1
'''
#Write a Python program to print all even numbers between 1 and 200.
'''
count9=1
while count9<=200:
    if count9%2==0:
        print(count9,"Evven number")
    count9+=1
'''
#Write a Python program to print numbers from 10 to 100 with an increment of 5.
'''
count10=1
while count10<=100:
    print(count10)
    count10+=5
'''
# Write a Python program to print numbers from 200 to 100 with a decrement of 10.
'''
count11=200
while count11>=100:
    print(count11)
    count11-=10
'''
#Q8. Write a Python program to print all numbers between 1 and 200 that are divisible by both 3 and 5. 
'''
count12=1
while count12<=200:
    if count12%3==0 and count12%5==0:
        print(count12)
    count12+=1
'''
#Write a Python program to print all numbers between 1 and 150 that are divisible by 7 but not divisible by 2. 
'''
count13=1
while count13<=150:
    if count13%7==0 and count13%2!=0:
        print(count13)
    count13+=1
'''
#Q10. Write a Python program to print all numbers between 1 and 100 that are divisible by either 4 or 6. 
'''
count14=1
while count14<=100:
    if count14%4==0 and count14%6==0:
        print(count14)
    count14+=1
'''
#Write a Python program to print all numbers between 1 and 300 that are divisible by 3, 5, and 10. 
'''
count15=1
while count15<300:
    if count15%3==0 and count15%5==0 and count15%10==0:
        print(count15)
    count15+=1
'''
#Q12. Write a Python program to print all numbers between 50 and 200 that are not divisible by 3. 
'''
count16=50
while count16<200:
    if count16%3!=0:
        print(count16)
    count16+=1
'''
#Q13. Write a Python program to print numbers from 1 to 100 and display whether each number is even or odd.    
'''
count17 = 1

while count17 <= 100:
    if count17 % 2 == 0:
        print(count17, "is Even")
    else:
        print(count17, "is Odd")

    count17 += 1
'''
#Q14. Write a Python program to print numbers from 1 to 100 and display:
#● "Divisible by 3" if the number is divisible by 3.
#● "Divisible by 5" if the number is divisible by 5.
# "Divisible by both" if divisible by both 3 and 5.
# "Not divisible" otherwise. 
'''
count18 = 1

while count18<= 100:
    if count18 % 3 == 0 and count18 % 5 == 0:
        print(count18, "Divisible by both")
    elif count18 % 3 == 0:
        print(count18, "Divisible by 3")
    elif count18 % 5 == 0:
        print(count18, "Divisible by 5")
    else:
        print(count18, "Not divisible")

    count18 += 1
'''
#Q15. Write a Python program to print numbers from 1 to 100 and identify whether each number is:
#● Even and divisible by 4.
#● Odd and divisible by 3.
#● Neither of the above. 
'''
i = 1

while i <= 100:
    if i % 2 == 0 and i % 4 == 0:
        print(i, "Even and divisible by 4")

    elif i % 2 != 0 and i % 3 == 0:
        print(i, "Odd and divisible by 3")

    else:
        print(i, "Neither of the above")

    i += 1
'''
#Q16. Write a Python program to print numbers from 1 to 150. Display "Small" for numbers below 50, "Medium" for numbers between 50 and 100, and "Large" for numbers above 100.
'''
i = 1

while i <= 150:
    if i < 50:
        print(i, "Small")

    elif i <= 100:
        print(i, "Medium")

    else:
        print(i, "Large")

    i += 1
'''
#Q17. Write a Python program to print numbers from 1 to 100. Display:
 #   ● "Multiple of 2" for numbers divisible by 2.
  #  ● "Multiple of 3" for numbers divisible by 3.
   # ● "Multiple of both 2 and 3" for numbers divisible by both.
   # ● "Other" for remaining numbers.
'''
i = 1

while i <= 100:
    if i % 2 == 0 and i % 3 == 0:
        print(i, "Multiple of both 2 and 3")

    elif i % 2 == 0:
        print(i, "Multiple of 2")

    elif i % 3 == 0:
        print(i, "Multiple of 3")

    else:
        print(i, "Other")

    i += 1
'''
#Q18. Write a Python program to calculate the sum of all numbers from 1 to 100 using a while loop.
'''
i = 1
total = 0

while i <= 100:
    total = total + i
    i += 1

print("Sum of numbers:", total)
'''
#Q19. Write a Python program to calculate the sum of all even numbers between 1 and 100.
'''
i = 1
total = 0

while i <= 100:
    if i % 2 == 0:
        total = total + i

    i += 1

print("Sum of even numbers:", total)
'''
#Q20. Write a Python program to calculate the sum of all odd numbers between 1 and 100.
'''
i = 1
total = 0

while i <= 100:
    if i % 2 != 0:
        total = total + i

    i += 1

print("Sum of odd numbers:", total)
'''
#Q21. Write a Python program to count how many numbers between 1 and 200 are divisible by 7.
'''
i = 1
count = 0

while i <= 200:
    if i % 7 == 0:
        count += 1

    i += 1

print("Count:", count)
'''
#Q22. Write a Python program to count how many even and odd numbers are present between 1 and 100.
'''
i = 1
even = 0
odd = 0

while i <= 100:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

    i += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
'''
#Q23. Write a Python program to calculate the sum of all numbers between 1 and 100 that are divisible by both 3 and 7
'''
i = 1
total = 0

while i <= 100:
    if i % 3 == 0 and i % 7 == 0:
        total = total + i

    i += 1

print("Sum:", total)
'''
#Q24. Write a Python program to print the multiplication table of 7 using a while loop (7 × 1 to 7 × 10).
'''
i = 1

while i <= 10:
    print("7 x", i, "=", 7 * i)

    i += 1
'''
#Example no 25
'''
i = 1
j=1

while i <= 10:
    j = 1

    while j <= i:
        print(j, end="")

        j += 1

    print()
    i += 1
'''
#Q26. Write a Python program to print all numbers between 1 and 500 whose last digit is 5.
'''
i = 1

while i <= 500:
    if i % 10 == 5:
        print(i)

    i += 1
'''
#Q27. Write a Python program to find and print all numbers between 1 and 100 that are divisible by 2, 3, and 5 simultaneously. 
'''
i = 1

while i <= 100:
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        print(i)

    i += 1
'''
#Q28. Write a Python program to calculate the product of all numbers from 1 to 10 using a while loop.
'''
i = 1
product = 1

while i <= 10:
    product = product * i

    i += 1

print("Product:", product)
'''
#Q29. Print numbers between 1 and 100 divisible by 2 or 5, but not both.
'''
i = 1

while i <= 100:
    if (i % 2 == 0 and i % 5 != 0) or (i % 2 != 0 and i % 5 == 0):
        print(i)

    i += 1
'''
#Q30. Write a Python program to count the total number of numbers between 1 and 500 that are:
#● Divisible by 3.
#● Divisible by 5.
#● Divisible by both 3 and 5. 
'''
i = 1


count3 = 0
count5 = 0
count_both = 0

while i <= 500:

    if i % 3 == 0:
        count3 += 1

    if i % 5 == 0:
        count5 += 1

    if i % 3 == 0 and i % 5 == 0:
        count_both += 1

    i += 1

print("Divisible by 3:", count3)
print("Divisible by 5:", count5)
print("Divisible by both 3 and 5:", count_both)

while i <= 500:

    if i % 3 == 0:
        count3 += 1

    if i % 5 == 0:
        count5 += 1

    if i % 3 == 0 and i % 5 == 0:
        count_both += 1

    i += 1

print("Divisible by 3:", count3)
print("Divisible by 5:", count5)
print("Divisible by both 3 and 5:", count_both)
'''



