class Person(object):
    #constructor
    def __init__(self, name):
        self.name = name
    #To gate name
    def getName(self):
        return self.name
    #to check if the person is an employee
    def isEmployee(self):
        return False
#inheritance of subclass (Note person is bracket)
class Employee(Person):
    #Here we return true
    def isEmployee(self):
        return True
#driver code
emp = Person("Geek1")
#An object of Person
print(emp.getName(), emp.isEmployee())
emp = Employee("Geek2")
#An object of Employee
print(emp.getName(), emp.isEmployee())
