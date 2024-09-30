# 1. Write a python program to display a user entered name followed by Good 
#                                         Afternoon using input () function. 
# 2. Write a program to fill in a letter template given below with name and date. 
#                        letter = '''  
#                        Dear <|Name|>, 
#                        You are selected! 
#                        <|Date|> 
#                         ''' 
# 3. Write a program to detect double space in a string. 
# 4. Replace the double space from problem 3 with single spaces. 
# 5. Write a program to format the following letter using escape sequence 
#                                                              characters. 
#                         letter = "Dear Harry, this python course is nice. Thanks!"

# --------------------------------------------------1
string = "good afternoon 'name'!"
Name = input()
string = string.replace("'name'",Name)
print(string)
bb="brooo"
print(f"good night , {bb}") # new thing add in python use F in print function 


# -------------------------------------------------2
letter = '''  
                        Dear <|Name|>, 
                        You are selected! 
                        <|Date|> 
                        ''' 
letter = letter.replace("<|Name|>","sumit").replace("<|Date|>","05 may 2006")
print(letter)
# -------------------------------------------------3

sss = "this  text contain  the double  space between it  now we try to find it "
ss = sss.find("  ")
print(ss)

# ------------------------------------------------4
 
#  same as 1,2 use replace 

# --------------------------------------------------5

#    use \n and \t in the well define the format 