import array
fruits = ["apple", "banana", "cherry"]
cars =["Ford", "BMW", "Volvo"]
print(f"before array extended {fruits}")
fruits.extend(cars)
print("after array extended")
print(fruits)
x = fruits.index("Ford")
print(x)
fruits.insert(1, "orange")
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
#sort using length
def myFunc(e):
    return len(e)
car = ['Ford', 'Mitsubisi', 'BMW', 'VM']
car.sort(key=myFunc)
print(car)