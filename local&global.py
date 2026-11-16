#Example no 1
'''


x=10
def function1():
    y=20
    print("locally,inside the function1,x=",x)
    print("locally,inside the function1,y=",y)
    #print("locally inside the function 1 z=",z)
def function2():
    z=30
    print("locally,inside the function2,x=",x)
    #print("locally,inside the function2,y="y)
    print("locally inside the function2,z=",z)
function1()
function2()
'''
#Example no 2
'''
x=10
def function():
    x=20
    print("locally,inside the function,x=",x)
function()
print("globally outside the function,x=",x)
'''


