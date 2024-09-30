'''
1. Write a program to print multiplication table of a given number using for loop. 
2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
    with S. 
    l = ["Harry", "Soham", "Sachin", "Rahul"] 
3. Attempt problem 1 using while loop. 
4. Write a program to find whether a given number is prime or not. 
5. Write a program to find the sum of first n natural numbers using while loop. 
6. Write a program to calculate the factorial of a given number using for loop. 
7. Write a program to print the following star pattern. 
      * 
     *** 
    *****  for n = 3 
8. Write a program to print the following star pattern: 
    * 
    ** 
    ***      for n = 3 
9. Write a program to print the following star pattern. 
    * * * 
    *   *   for n = 3 
    * * *  
10. Write a program to print multiplication table of n using for loops in reversed 
    order.
'''
# --------------------------------------------------------------------------------1
'''
a = int(input("enter the no. you want to print the table "))
for i in range (1,11):
    print(F"{a} X {i} = {a*i}")
''' 
# --------------------------------------------------------------------------------2
'''
l = ["Harry", "Soham", "Sachin", "Rahul"] 
for name in l:
    if (name.startswith("S")):
        print(F"hello {name}")
'''

# ---------------------------------------------------------------------------------3
'''
a = int (input("enter the no. you want to print the table "))
i = 1
while(i<=10):
    print(F"{a}X{i}={a*i}")
    i = i+1
    '''
# --------------------------------------------------------------------------------4
'''
a = int (input("enter the no. to check the no. is prime or not "))
for i in range (2,a):
    if(a%i)==0:
        print("Number is not prime ")
        break
    else:
        print("the no. is prime ")
'''
# -------------------------------------------------------------------------------5
'''
a = int(input("enter a no. to want the sum of 1 to N: "))
i=1
sum=0
while(i<=a):
    sum+=i
    i+= 1
print(sum)
'''
# ---------------------------------------------------------------------------------6
'''
a = int(input("enter a no. to want the sum of 1 to N: "))
product=1
for i in range (1,a+1):
    product=product*i
print(product)
'''
# ---------------------------------------------------------------------------------7
'''
n = int(input("enter the value of n: "))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1), end="")
    print("")
'''

# -----------------------------------------------------------------------------------8
'''
n = int(input("enter the value of n: "))

for i in range(1,n+1):
    print(" "*(n-i),)
    print("*"*i, end="")
    print("")
    
'''
# ------------------------------------------------------------------------------------9
'''
n = int(input("enter the value of n: "))

for i in range(1,n+1):
    if (i==1 or i ==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")
'''
# -------------------------------------------------------------------------------------10
'''
n = int(input("enter a no.: "))

for i in range(1,11):
    print(f"{n}X{11-i}={n*(11-i)}")
''' 
# ====end=====end======end=======end=======end======end=======end=====end====end======end