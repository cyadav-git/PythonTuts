num=[
    [23,45,43,23,45],
    [45,67,54,45,44],
    [89,90,87,65,44],
    [23,45,67,32,45]
]
print(f"The given array is {num}")
#print second row second column
print(num[1][1])
#print the whole 2d matrix
for row in num:
    for col in row:
        print(col, end=" ")
    print()


rows, cols = (5,5)
arr = [
    [0 for i in range(cols)]
    for j in range(rows)
]
print(arr)

rows, cols = (5,5)
arr=[]
for i in range(rows):
    col=[]
    for j in range(cols):
        col.append(0)
    arr.append(col)
print(arr)