import os
import shutil
import datetime
#use to create the directory if not exist
import time

if not os.path.isdir("help"):
    os.mkdir("help")
#change the current working directory
os.chdir("D:\PythonWithDjango\chandan\help")
#create the file helpme.txt on the current working directory
file = open('helpme.txt', 'w')
file.close()

print(os.listdir("D:\PythonWithDjango\chandan\help"))
#get the info about the current working directory
print(os.getcwd())
os.chdir("D:\PythonWithDjango\chandan")
print(os.getcwd())
#deletes the all files and the specified directory
if shutil.rmtree('help'):
    print("the directory is deleted")
else:
    print("directory is not found")
#os.rmdir("help")
date_now = datetime.datetime.now()
print(date_now)
date_object = datetime.date.today()
print(date_object)
print(dir(datetime))0
now = datetime.datetime.now()
d = now.strftime("%Y/%m/%d")
print("today:",d)
t = now.strftime("%H:%M:%S")
print("current time:", t)