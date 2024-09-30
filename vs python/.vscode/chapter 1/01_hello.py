#  chaptre 2 
 # problem no. 1
# a = input ("enter the first no: ")
# b = input ("enter the second no: ")
# c=44
# d = 3
# print("the sum the no. is ",c + d)
# print ("the sum of a and b is ", a +b)
# # print ("the sum of a and c is ", a + c)
# print ("the sum of two no. is ",int (a) + int(b) )

# print ("the remainder when divide by 2 is " ,int(a)%2)
# a = 34
# b = 80
#  c= (a ==b)
#  print (a==b)
# print("the average of this two no. is a",int(a)," and b is ",int(b),(int (a)+int (b))/2)
# print ("the square of the no. is ", float(a)**2)


# -----------------------------------------------------------------------------------------------------------------------------

# chapter 3
# concatination string 
# greeting = "good morning, "
# name = 'sumit '
# print (greeting+name)
# name = "sumit"
# print (name [0])


# practise set chapter 3
#   question 1
# name = input ("enter your name ")
# print ("good after noon "+name )

# question 2 
# letter = '''dear <|name|>,
#  you are selected
# date: <|date|>'''

# name = input("enter your name ")
# date = input("enter date")
# letter=letter.replace("<|name|>",name)
# letter=letter.replace("<|date|>",date)
# print(letter)

# question 3,4
# text = "the text  contain  double space between the words  now we replce it by  single  space "
# print (text)
# boolee=text.find("  ")
# print(boolee)
# text= text.replace("  "," ")
# print (text)

# question 5
# letter = ('"Dear Harry, this python course is nice. Thanks!"')
# print (letter)

# ----------------------------------------------------------------------------------------------------------
# list and typles 
# sumit= ["sumit","wants","to","make","world","number",1,"in computer program "]
# print (sumit[0])
# l1= [1,8,7,2,21,15]
# l1.sort()
# print(l1)
# l1.reverse()
# print (l1)
# l1.append(8)
# print(l1)
# l1.clear()
# print (l1)

# ----------------------------------------------------------------------------------------------------------
# practise set 4
# question 1
# f1= input("enter the fruit no. 1 ")
# f2= input("enter the fruit no. 2 ")
# f3= input("enter the fruit no. 3 ")
# f4= input("enter the fruit no. 4 ")
# f5= input("enter the fruit no. 5 ")
# f6= input("enter the fruit no. 6 ")
# f7= input("enter the fruit no. 7 ")
# my_fruit_list = [f1,f2,f3,f4,f5,f6,f7]
# print(my_fruit_list)
# ------------------------------------------
# practise question 2
# m1= int(input("enter the student marks  no. 1 "))
# m2= int(input("enter the student marks  no. 2 "))
# m3= int(input("enter the student marks  no. 3 "))
# m4= int(input("enter the student marks  no. 4 "))
# m5= int(input("enter the student marks  no. 5 "))
# m6= int(input("enter the student marks  no. 6 "))
# marks = [m1,m2,m3,m4,m5,m6]
# print(marks)
# marks.sort()
# print(marks)
# --------------------------------------------
# question 3
# a=(3,4,6,7,3,67,)
# a[0]=643           give typing error
# --------------------------------------------
# question 4
# a = [3,6,7,4]
# print(a[0]+a[1]+a[2]+a[3])
# --------------------------------------------
# question 5
# a=(7,0,8,0,0,9)
# print(a.count(0))
# --------------------------------------------------------------------------------------------------------
# chapter 6
# age= int(input("enter your age"))
# if (age>18):
#     print("yes")
# else:
#     print("no") 
n1= int(input("enter the first no. "))
n2= int(input("enter the second no. "))
n3= int(input("enter the third no. "))
n4= int(input("enter the fourth no. "))
if (n1>n2 and n2>n3 and n3>n4):
    print("the first no. is greater: ")
    print(n1)
if (n1<n2 and n2>n3 and n3>n4):
    print("the second no. is largest: ")
if (n1<n2 and n2<n3 and 
    )