class employee:
    name = "sumit"# class attribute
    language = "python"
    salary = 1200000
    
    def __init__(self):# dunder method which is automatic call start with -- 
        print("i am creating an object ")
    
    def getinfo(self):
        print(f"the language is {self.language}. the salary is {self.salary} the name is {self.name}")
    @staticmethod # abb hamai yaha koii bhi self nahi likhna 
    def greet():
        print("good morning")

harry = employee()
harry.name= "kya haal hai "# instance attribute
print (harry.name,harry.salary,harry.language)# hare name is instance attribute because instance has 
                                            # more preference than class attribute
harry.getinfo()
harry.greet()
