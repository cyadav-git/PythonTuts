import os
#renaming the file name
if os.path.exists('newfile.txt'):
    os.rename('newfile.txt', 'rename.txt')
#deleting the file
if os.path.exists('rename.txt'):
    os.remove('rename.txt')

path = "admin"
isExist = os.path.exists(path)
if not isExist:
    os.makedirs(path)
    print(path, "directory created")
else:
    print(path, "admin directory already exists")
print(os.listdir("admin"))
#print(os.listdir("D:\PythonWithDjango\chandan"))

for x in os.listdir("D:\PythonWithDjango\chandan"):
    print(x)
for x in os.listdir("D:\PythonWithDjango\chandan"):
    if os.path.isfile(x): print('File -', x)
    elif os.path.isdir(x): print("Directory -", x)
    else: print("----", x)
#programs to show various ways to read and write data.
#creating a file,
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

#writing data to a file
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes.

file1 = open("myfile.txt", "r+")
print("Output of Read function is ")
print(file1.read())
print()

#seek(n) takes the file handle to the nth
#bite from the beginning.
file1.seek(0)
print("Output of Readline function is ")
print(file1.readline())
print()
file1.seek(0)
#To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()
file1.seek(0)
print("Output of Readline(9) function is ")
print(file1.readline(9))
print()
file1.seek(0)
#readlines functions
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.seek(0)