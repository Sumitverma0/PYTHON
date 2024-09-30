import random
'''
1 for snake
-1 for water
0 for gun '''
computer= random.choice([0,1,-1])# yai ak random no genetrate karaiga 
youstr=input("enter your choice(s,w,g):.. ")
youdict= {"s":1,"w": -1,"g": 0}
revdict= {1:"snake",-1:"water",0:"gun"}

you=youdict[youstr]
print(f"your choice {revdict[you]}\ncomputer choice {revdict[computer]}")

if (computer==you):
    
    print("kya yarr draw ho gaya match fir sai try karoo ")
    
else:
    
    '''
    here the logic is dovelop making all combination and check similirity we see that 
    at (computer - you ) then -1 or 2 is for lose then enstid of writting full if elif code
    we make it short form only four line code..........'''
    
    
    if ((computer-you)==-1 or (computer-you)==2):
        print("you lose !")
    else:
        print("you win!")