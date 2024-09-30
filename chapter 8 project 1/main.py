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
    
    if (computer == 1 and you==0):
        print("you win!")
    elif(computer==1 and you ==-1):
        print("you loss !")


    elif(computer==0 and you ==-1):
        print("you win!")
    elif(computer==0 and you ==1):
        print("you loss !")


    elif(computer==-1 and you ==1):
        print("you win!")
    elif(computer==-1 and you ==0):
        print("you loss !")


    else:
        print("something is wrong plzz try again")
