def absolute_value(num):
    """
    this function returns the absolute
    value of the entered number
    """
    if num >= 0:
        return num
    else:
        return -num

print(absolute_value(2))
print(absolute_value(-4))

#variable life time
def my_func():
    x = 10
    print("the value of inside function :", x)
x = 20
my_func()
print("the value of outside function :", x)

#function with return

def sum(num1, num2):
    sum = num1+num2
    return sum
number1 = 30
number2 = 50
total = sum(number1, number2)
print(f"the sum of {number1} and {number2} is {total}")

#function with default argument
def sum1(num1=10, num2=30):
    sum = num1+num2
    return sum
total = sum1()
print(f"the total of is {total}")

#arbitrary argument

def greet(*names):
    """
    This function greets all
    the person in the names tuple.
    """
    #names is a tuple with arguments
    for name in names:
        print("Hello", name)
greet("monica", "Luke", "Steve", "John")

#nonlocal function variable
#this means that the variable can be neither in the local nor the global scope.
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

#making local variable global.

c = 2
def add():
    global c
    c = c+2
    print("inside add():", c)
add()
print("in main", c)

#function examples
#function defination
def greet(name):
    # docstring function discription
    """
    this function greets to the person
    passed in as
    a parameter
    """

    #function statement
    print("Hello, " + name + ". Good morning!")
name = input("Enter the Name: ")
#function call
greet(name)