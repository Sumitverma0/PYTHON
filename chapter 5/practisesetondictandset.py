'''
1. Write a program to create a dictionary of Hindi words with values as their English 
    translation. Provide user with an option to look it up! 
2. Write a program to input eight numbers from the user and display all the unique 
    numbers (once). 
3. Can we have a set with 18 (int) and '18' (str) as a value in it? 
4. What will be the length of following set s: 
    s = set() 
    s.add(20) 
    s.add(20.0) 
    s.add('20') # length of s after these operations? 
5. s = {} 
    What is the type of 's'? 
6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
    value and use key as their names. Assume that the names are unique. 
7. If the names of 2 friends are same; what will happen to the program in problem 6? 
8. If languages of two friends are same; what will happen to the program in problem 6? 
9. Can you change the values inside a list which is contained in set S? 
    s = {8, 7, 12, "Harry", [1,2]}
'''

# ---------------------------------------------------------1
'''
words ={
    "madat":"help",
    "khushi":"happy",
    "love":"krishna"
}

print(words.keys())
w = input("enter the key you want to know the meaning of that key: ")
print(words[w]) 
'''

# -------------------------------------------------------------2
'''
s=set()
n=int(input("enter the no: "))
s.add(n)
n=int(input("enter the no: "))
s.add(n)
n=int(input("enter the no: "))
s.add(n)
n=int(input("enter the no: "))
s.add(n)
n=int(input("enter the no: "))
s.add(n)
n=int(input("enter the no: "))
s.add(n)
n=int(input("enter the no: "))
s.add(n)
print(s)
'''
# ---------------------------------------------3
'''
s=set()
s.add(18)
s.add("18")
print(s)

'''
# ----------------------------------------------4
'''
s = set() 
s.add(20) 
s.add(20.0) # 1 == 1.0 is True
s.add('20')
print(s)

'''
# ------------------------------------------------5
s = {}
print(type(s))

# ------------------------------------------------6

# 6,7,8 easyyyyy

# -------------------------------------------------9
'''
s = {8, 7, 12, "Harry", [1,2]}
no you can not change it question 9
'''

