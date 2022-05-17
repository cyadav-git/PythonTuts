class Dog:
    #class attributes
    attr1 = "mammal"
    attr2 = "dog"
    #class method
    def fun(self):
        print("I'm a ", self.attr1)
        print("I'm a ", self.attr2)
#object instantiation
Rodger = Dog()

#accessing class attributes
#and method through objects.
print(Rodger.attr1)
Rodger.fun()