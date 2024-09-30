'''
1. Write a program to find the greatest of four numbers entered by the user. 
2. Write a program to find out whether a student has passed or failed if it requires a 
    total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
    take marks as an input from the user. 
3. A spam comment is defined as a text containing following keywords: 
    "Make a lot of money", "buy now", "subscribe this", "click this". Write a program 
    to detect these spams. 
4. Write a program to find whether a given username contains less than 10 
    characters or not. 
5. Write a program which finds out whether a given name is present in a list or not. 
6. Write a program to calculate the grade of a student from his marks from the 
    following scheme: 
    90 – 100 => Ex 
    80 – 90 => A 
    70 – 80 => B 
    60 – 70  =>C 
    50 – 60 => D 
    <50        
    => F 
7. Write a program to find out whether a given post is talking about "Harry" or not.
'''
# ---------------------------------------------------------------------------1
'''
a1=int(input("enter a no: "))
a2=int(input("enter a no: "))
a3=int(input("enter a no: "))
a4=int(input("enter a no: "))
if(a1>a2 and a1>a3 and a1>a4):
    print(a1,"is greater")
elif(a2>a1 and a2>a3 and a2>a4):
    print(a2,"is greater")
elif(a3>a1 and a3>a2 and a3>a4):
    print(a3,"is greater")
else:
    print(a4,"is greater")
    '''
# ---------------------------------------------------------------------------2
'''
a1=int(input("enter marks of your subject1: "))
a2=int(input("enter marks of your subject2: "))
a3=int(input("enter marks of your subject3: "))
# check total percentage 
total_percentage = (100*(a1+a2+a3))/300
if (total_percentage >= 40 and a1>33 and a2>33 and a3>33):
    print ("you are pass",total_percentage)
else:
    print ("congrats you fail, sad mat hoo yarr ",total_percentage)

'''
# ------------------------------------------------------------------------------3
'''
p1="Make a lot of money "
p2="buy now"
p3="subscribe this"
p4="click this"

message = input("enter your comment: ")
if((p1 in message)or(p2 in message)or(p3 in message)or(p4 in message)):
    print("abai spam kyoo kar raha hai ")
else:
    print("bhai abhi tak spam nahi kiya or karyioo bhi mat samjaaa ")
'''
# -------------------------------------------------------------------------------4
'''
user_name = input("name daal apna: ")
if (len(user_name)>10):
    print("taira name valid hai manai check kiya abi ")
else:
    print("taira name mai 10 character nahi hai too taira name valid nahi hai ")
'''
# --------------------------------------------------------------------------------5
'''
l1= ["harry","sumit","jjjjj","divya"]
name= input("enter your name ")
if (name in l1):
    print("YOUR NAME IS IN LIST")
else:
    print("not found your name in the list")
'''

# -------------------------------------------------------------------------------6
'''
marks = int(input("enter your marks "))
if (marks<=100 and marks>=90):
    print("EX")
elif(marks<=89 and marks>=)
...................................ho jaiga yarr easy question 


'''
# -------------------------------------------------------------------------7
'''
easy hai yarr
input and if loop harry in post and remember Harry in it 
# some trick is in if loop write like ("Harry".lower() in post.lower()):
# then it will check all posiblity of HaRry, harrry , hArry ...
the trick is input koo change in lower case and post koo bhi then check it '''