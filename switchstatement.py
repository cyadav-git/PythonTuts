#switch statement in python
def SwitchExample(argument):
    switcher = {
        0: "This is case zero",
        1: "This is case one",
        2: "This is case Two"
    }
    return switcher.get(argument, "nothing")
if __name__ == "__main__":
    argument = 0
    print(SwitchExample(argument))

#While Loop
x=0
while(x <10):
    print(x)
    if x==5:
        break
    x = x+1

x=0
while(x <10):
    x = x + 1
    if x==3:
        continue
    print(x)
#for loop

for y in range(6):
    if y == 3:
        break
    print(y)
else:
    print("Finished")

#Nested for loop
adj = ['red','big','testy']
fruits = ['apple','banana','cherry']
for x in adj:
    for y in fruits:
        print(x, y)