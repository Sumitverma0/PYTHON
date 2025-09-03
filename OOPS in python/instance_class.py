class Emoployee: #class
    company='Asus' # this is class attrubute
    def __init__(self,name,salary,company):  #constructor
        self.name=name
        self.salary=salary
        self.company=company
    
    def get_salary(self): # method of the class 
        return self.salary
        
    def get_info(self):
        print(f"the name is {self.name} ,the salary is {self.salary} and the company name is {self.company}")

e=Emoployee('john',42000,'tesla') # object 
# print(e.get_salary())
print(e.company)# will always print instance attribute
print(dir(e))