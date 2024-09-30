'''
1. Write a program using functions to find greatest of three numbers. 
2. Write a python program using function to convert Celsius to Fahrenheit. 
3. How do you prevent a python print() function to print a new line at the end. 
4. Write a recursive function to calculate the sum of first n natural numbers. 
5. Write a python function to print first n lines of the following pattern: 
*** 
**               
* - for n = 3 
6. Write a python function which converts inches to cms. 
7. Write a python function to remove a given word from a list ad strip it at the same 
time. 
8. Write a python function to print multiplication table of a given number.
'''

# -----------------------------------------------------------------------------1
'''
a = int(input("enter first no: "))
b = int(input("enter second no: "))
c = int(input("enter third no: "))

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
print(f"the greatest between {a,b,c} is {greatest(a,b,c)}")
'''
# -----------------------------------------------------------------------------2
'''
                    #  formula is c = 5*(f-32)/9
def convert(f):
    c = 5*(f-32)/9
    return c
f = int(input("enter the temp in f: "))
print(f"the temp f to c is {convert(f)}")
'''
# -----------------------------------------------------------------------------3
'''
print("a")
print("b")
print("c",end="")
print("d",end="")
print("j",end="u")
print("check",end="hmm")
'''

# -----------------------------------------------------------------------------4
'''
def sum(n):
    if (n==1):
        return 1
    return sum(n-1)+n

n= int(input("enter a natural no: "))
print(f"the sum of 1 to  {n}th no. is {sum(n)}")
'''
# --------------------------------------------------------------------------------5
'''
def pattern(n):
    if (n==0):
        return
    print("*"*n)
    pattern(n-1)
    
n=int(input("enter a no "))

pattern(n)
'''
# ------------------------------------------------------------------------------6
'''
def inch_to_cm(n):
    return n*2.54
n=int(input("inch wali value daal "))
print(f"inch{n} sai cm mai convert ho gaya hai check kar lai {inch_to_cm(n)} ")
'''
# -----------------------------------------------------------------------------7
'''
l= ["sumit","codeX","jarvisX","krishna","X"]
def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n 
    
print(rem(l,"X"))
'''
# ---------------------------------------------------------------------------8

def multi(n):
    for i in range(1,11):
        print(f"{n}X{i}={n*i}")

n=int(input("enter the no. "))
multi(n)