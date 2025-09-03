class Emoployee: #class
    def __init__(self,name,salary):  #constructor
        self.name=name
        self.salary=salary
    
    def get_salary(self): # method of the class 
        return self.salary
        

e=Emoployee('john',42000) # object 
print(e.get_salary())