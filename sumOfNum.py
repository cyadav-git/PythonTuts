import array
num = int(input("Enter the number of times to input:"))
numbers = []
sum = 0;
for i in range(num):
    number = int(input(f"enter the number {i+1}:"))
    numbers.append(number)
    sum = sum+number
average = float(sum/num)
print(f"The user entered Numbers {numbers}")
print(f"The sum of the entered number is {sum}")
print(f"The average of the entered number is {average}")



