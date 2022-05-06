num1 = int(input("Enter the first num: "))
num2 = int(input("Enter the second num: "))
num3 = int(input("Enter the third num: "))
if(num1>num2 and num1>num3):
    print("The greatest number is {0}".format(num1))
elif(num2>num3 and num2>num1):
    print("The greatest number is {0}".format(num2))
else:
    print(num3)