#Return statement

#Example 1
'''
def greet():
    print("Greet function starts")
    print("Good evening")
    print("Greet function ends")
print(greet())
'''
#Example 2
'''
def lucky_number():
    return 5
x=lucky_number()
print(x)
'''

#Example 3
'''
def add(a,b):
    ans=a+b
    print(ans)
total=add(10,20)
print(total)
'''

#Example 4
'''
def add(a,b):
    ans=a+b
    return ans
total=add(10,20)
print(total)
'''
#Example 5
'''
def add(a,b):
    ans=a+b
    return ans
def sub(a,b):
    ans=a-b
    return ans
def mul(a,b):
    ans=a*b
    return ans
def div(a,b):
    ans=a/b
    return ans
c=add(10,20)
print("add=",c)
c=sub(10,20)
print("sub",c)
c=mul(10,20)
print("mul",c)
c=div(10,20)
'''
print("div",c)
