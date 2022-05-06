import array
balance =array.array('i',[200,300,400])
print(balance[1])
print(balance[-1])
#printing the all elements in the array list
for a in balance:
    print(a, end=" ")
print()
names = ["chandan","mukesh","purna","mina","sabin","nadim"]
print(names[2])
print("Last element in the array list is :",names[-1]) #print last element in the array list
print(names[1:5]) #range of array or slicing operation

names.insert(3,"mahesh")
print("updated array after inserted new array",names[1:5])
print(names[:])
#array modification(update array elements)
names[0]="ram"
print(names[:])
#array concatination
first = array.array('b',[4,5,6])
second = array.array('b',[7,8,9,10])
number = array.array('b')
number = first + second
print(number)
for i in number:
    print(i, end=" ")
names.pop(2)
print(names[:])
del names[3]
print(names[:])
print(len(names))
names.remove("ram")
print(names[:])