#file name test is open with read only mode from the source folder.
file = open('test.txt', 'r')
for each in file:
    print(each)
file = open(r"D:\read\test.txt", "r")
#this will print every line one by one in the file.
for hlp in file:
    print(hlp)
file.close()
file1 = open(r"D:\read\test.txt", "r")
#this will print every line one by one in the file.
print(file1.read())#read all the content in the file
print(file1.read(10)) #read only the given criteria of a file.
file1.close()

#python to override a file.
file = open('test.txt', 'w')
file.write("this is the write command \n")
file.write("It allows us to write in a particular file")
file.close()

