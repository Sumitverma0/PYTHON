'''
1.  Write a program to read the text from a given file ‘poems.txt’ and find out 
    whether it contains the word ‘twinkle’. 
2.  The game() function in a program lets a user play a game and returns the score 
    as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
    contains the previous Hi-score. You need to write a program to update the Hi
    score whenever the game() function breaks the Hi-score. 
3.  Write a program to generate multiplication tables from 2 to 20 and write it to the 
    different files. Place these files in a folder for a 13 – year old. 
4.  A file contains a word “Donkey” multiple times. You need to write a program 
    which replace this word with ##### by updating the same file.  
5.  Repeat program 4 for a list of such words to be censored. 
6.  Write a program to mine a log file and find out whether it contains ‘python’. 
7.  Write a program to find out the line number where python is present from ques 6. 
8.  Write a program to make a copy of a text file “this. txt” 
9.  Write a program to find out whether a file is identical & matches the content of 
    another file. 
10. Write a program to wipe out the content of a file using python. 
11. Write a python program to rename a file to “renamed_by_ python.txt.
'''
# -----------------------------------------------------------------------1
'''
f = open("06_poem.txt")
content=f.read()
if ("twinkle" in content):
    print("the word twinkle is present in content")
else:
    print("the word twinkle not present in content")
f.close()
'''

# --------------------------------------------------------------------------2
'''
import random

def game():
    print("you are playing the game: ")
    score=random.randint(1,62)
    # fetch the highscore 
    with open("07_hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"your score: {score}")
    if(score>hiscore):
        # write this hiscore to the file 
        with open("07_hiscore.txt","w") as f:
            f.write(str(score))
    return score
game()
'''
# ------------------------------------------------------------------------------------3

'''
def generateTable(n):
    table=""
    for i in range(1,11):
        table+=f"{n} X {i} = {n*i}\n"
    
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)
    '''
    
# -----------------------------------------------------------------------------------4
'''
word = "donkey"
with open("08_file.txt","r") as f:
    content = f.read()

content = content.replace("donkey","######")
with open("08_file.txt","w") as f:
    f.write(content)
'''

# ----------------------------------------------------------------------------------5
'''
words = ["donkey","hlo","check"]
with open("08_file.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#"*len(word))
with open("08_file.txt","w") as f:
    f.write(content)
'''
# -------------------------------------------------------------------------------6
'''
with open("09_log.txt") as f:
    content = f.read()

if ("python" in content):
    print("yes python is present in 09_log.txt")
else:
    print("no python is not present")
    '''

# ---------------------------------------------------------------------------------7
'''

with open("09_log.txt") as f:
    lines = f.readlines()

lineno=1 
for line in lines:
    if ("python" in line):
        print(f"yes python is present in 09_log.txt line no. is {lineno}")
        break
    lineno=lineno+1 

else:
    print("no python is not present")
'''

# --------------------------------------------------------------------------------8
'''
with open("10_this.txt") as f:
    content = f.read()
    
with open("10_thiscopy.txt","w") as f:
     f.write(content)
     '''
     
# ---------------------------------------------------------------------------------9
'''
with open("10_this.txt") as f:
    content1 = f.read()
    
with open("10_thiscopy.txt") as f:
    content2 = f.read()

if (content1==content2):
    print("yes this two  file are identical ")
else:
    print("not this two file are not identical ")
'''

# --------------------------------------------------------------------------------10
'''
with open("10_thiscopy.txt","w") as f:
     f.write("")# abb 10_thiscopy.txt ka data wipe matlab delete ho gaya...
'''

# --------------------------------------------------------------------------------11

with open("11_old.txt") as f:
    content = f.read()
    
with open("11_rename_old.txt","w") as f:
     f.write(content)
#  abb hmm  (import os) module kaa use kar kai  original file koo delete kar 
# saktai hai kudh sai by some research yaa fir (sh util) module kaa use 