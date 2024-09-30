class employee:
    company = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

'''        
class programmer:
    company = "ITC Infotech"
    def show(self):
        print (f"the name is {self.name} and the salary is {self.salary}")
        
    def showlanguage(self):
        print (f"the name is {self.name} and he is good with {self.language} language")
        
'''

# using inheritance 

class programmer(employee):
    company = "ITC Infotech"
    def showlanguage(self):
        print (f"the name is {self.name} and he is good with {self.language} language")
        
        
        
a = employee()
b = programmer()
print(a.company,b.company) 