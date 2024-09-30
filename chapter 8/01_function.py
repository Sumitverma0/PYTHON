# function definition
'''
def avg():
    a=int(input("enter a no: "))
    b=int(input("enter 2 no: "))
    c=int(input("enter 3 no: "))
    average=(a+b+c)/3
    print(average)
# fuction call
avg()


def good_day(name):
    print("good day " + name)

good_day("sumit ")
'''

# recursion  
def factorial(n):
    if ((n==0) or (n==1)):
        return 1
    return n * factorial(n-1)
n=int (input("ak no dal bai: "))
print(f"the factorial of {n} is : {factorial(n)}")