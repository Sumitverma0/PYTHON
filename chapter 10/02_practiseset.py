'''
1. Create a class “Programmer” for storing information of few programmers 
    working at Microsoft. 
2. Write a class “Calculator” capable of finding square, cube and square root of a 
    number. 
3. Create a class with a class attribute a; create an object from it and set ‘a’ 
    directly using ‘object.a = 0’. Does this change the class attribute? 
4. Add a static method in problem 2, to greet the user with hello. 
5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
    and get fare information of train running under Indian Railways. 
6. Can you change the self-parameter inside a class to something else (say 
    “harry”). Try changing self to “slf” or “harry” and see the effects.
'''

# ------------------------------------------------------------------------------1
'''
class programmer:
    company= "microsoft"
    def __init__(self,name,salary,pincode):
        self.name=name
        self.salary= salary
        self.pincode= pincode

p = programmer("sumit",2400000,221709 )
print(p.name,p.salary,p.company,p.pincode)

r = programmer("rohan",2402000,221729 )
print(r.name,r.salary,r.company,r.pincode)
'''
# ---------------------------------------------------------------------------------2
'''
class calculator:
    def __init__(self,n):
        self.n=n
    def sqr(self):
        print(f"the squre of {self.n} is {self.n*self.n}")
        
    def cube(self):
        print(f"the cube of {self.n} is {self.n*self.n*self.n}")
        
    def sqrroot(self):
        print(f"the squreroot of {self.n} is {self.n**1/2}")


a= calculator(4)
a.sqr()
a.cube()
a.sqrroot()
'''

# -------------------------------------------------------------------------3
'''
class demo:
    a= 4

o= demo()
print(o.a)
o.a=0
print(o.a)# no this no change the class attributes
print(demo.a)
'''

# -------------------------------------------------------------------------4
'''
class calculator:
    def __init__(self,n):
        self.n=n
    @staticmethod
    def greeet():
        print("hello bhai this is static method without self argument")
    def sqr(self):
        print(f"the squre of {self.n} is {self.n*self.n}")
        
    def cube(self):
        print(f"the cube of {self.n} is {self.n*self.n*self.n}")
        
    def sqrroot(self):
        print(f"the squreroot of {self.n} is {self.n**1/2}")


a= calculator(4)
a.greeet()
a.sqr()
a.cube()
a.sqrroot()
'''
# ----------------------------------------------------------------------------5
'''
from random import randint 
class train:
    def __init__(self,trainno):
        self.trainno =trainno
        
    def book(self,trainno,fro,to):
        print(f"ticket is booked in train no {self.trainno} from {fro} to {to} ")
    
    def getstatus(self,trainno):
        print(f"ticket is booked in train no {self.trainno} is running on time ")
    
    def getfare(self,trainno,fro,to):
        print(f"ticket fare in train no: {self.trainno} from: {fro} to: {to} is {randint(222,555)}")
        
t = train (14006)
t.book(14006,"new delhi","ballia")
t.getfare(14006,"delhi", "ballia")
t.getstatus(14006)
'''
# --------------------------------------------------------------------6

from random import randint 
class train:
    def __init__(slf,trainno):
        slf.trainno =trainno
        
    def book(self,trainno,fro,to):
        print(f"ticket is booked in train no {self.trainno} from {fro} to {to} ")
    
    def getstatus(self,trainno):
        print(f"ticket is booked in train no {self.trainno} is running on time ")
    
    def getfare(self,trainno,fro,to):
        print(f"ticket fare in train no: {self.trainno} from: {fro} to: {to} is {randint(222,555)}")
        
t = train (14006)
t.book(14006,"new delhi","ballia")
t.getfare(14006,"delhi", "ballia")
t.getstatus(14006)