# 1. Write a program to store seven fruits in a list entered by the user. 
# 2. Write a program to accept marks of 6 students and display them in a sorted manner.
# 3. Check that a tuple type cannot be changed in python. 
# 4. Write a program to sum a list with 4 numbers. 
# 5. Write a program to count the number of zeros in the following tuple: 
#                           a = (7, 0, 8, 0, 0, 9) 


# -------------------------------------------------------1
# f1=input("enter the fruits name 1: ")
# f2=input("enter the fruits name 2: ")
# f3=input("enter the fruits name 3: ")
# f4=input("enter the fruits name 4: ")
# f5=input("enter the fruits name 5: ")
# f6=input("enter the fruits name 6: ")
# f7=input("enter the fruits name 7: ")
# lis=[f1,f2,f3,f4,f5,f6,f7]
# print(lis)
'''2 method of first question 
  fruit=[]
  f1 = input("enter the fruit name ")
  fruit.append(f1)
  continue up to seven times

  '''

# -----------------------------------------------------------2

# f1=int(input("enter the student no. 1: "))
# f2=int(input("enter the student no. 2: "))
# f3=int(input("enter the student no. 3: "))
# f4=int(input("enter the student no. 4: "))
# f5=int(input("enter the student no. 5: "))
# f6=int(input("enter the student no. 6: "))

# lis=[f1,f2,f3,f4,f5,f6,]
# lis.sort()
# print(lis)

# -----------------------------------------------------------3

# tuple=(5,6,3,"sumit")
# tuple[0]="ju"
# TypeError: 'tuple' object does not support item assignment output......



# ----------------------------------------------------------4

l=[7,4,8,9,46,3]
print(sum(l))

# -----------------------------------------------------------5

a = (7, 0, 8, 0, 0, 9) 
print(a.count(0))

# now all setttttt...............