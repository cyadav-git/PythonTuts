file = open('test.txt', 'r+')
file.write("this is the w+ file \n")
file.write("this is the second line")
file.close()

with open("test.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

