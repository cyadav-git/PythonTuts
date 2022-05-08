import array
#append is used to add the new element in the array in the last.
fruits = ["apple", "Banana", "Cherry"]
fruits.append("orange")
print(fruits)

#The clear() method removes all the elements from a list.
print("after the clear function is run: ")
fruits.clear()
print(fruits)

#copy() mithod returns a copy of the specified list
fruits = ["Apple", "Banana", "Cherry", "Orange","cherry"]
print("after the copy operation is run")
x = fruits.copy()
print(x)

#count() method returns the number of elements with the specified value.
fruits = ["cherry", "cherry"]
x = fruits.count("cherry")
y = len(fruits)
print(x)
print(f"Total length of Fruits array is {y}")
#wap to ask the number of users
number = int(input("How many names you want to add:"))
names = []
for i in range(number):
    name = input("enter the name: ")
    names.append(name)
print(names)
search = input("enter the name for search: ")
count = names.count(search)
if count>=1:
    print(f"search {search} found")
else:
    print(f"search {search} not found")



