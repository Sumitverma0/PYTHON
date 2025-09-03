class Animal:
    location='loc'
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        print("speaking know... ")
        
class Dog(Animal):
    def speak(self):
        super().speak()  # here we call the parents class method also 
        print('woof')
        
# a=Animal('dog')
# a.speak()

b=Dog('dogesh')
print(b.location)
b.speak()