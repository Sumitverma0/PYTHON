'''
a= "a very long string with emails"
email=[]
'''

#1. file to read 
'''
f=open("02_filetxt.txt")
data = f.read()
print(data)
f.close()# imp f.close() because to close the file after task complete 
'''



#2. file to write
''' 
st="hey name how are you "
f=open("03_myfile.txt","w")
f.write(st)
f.close()

'''


#3. readeline 
'''
f= open("04_multiline.txt")
# lines= f.readlines()
# print(lines)
# print(type(lines))
line1=f.readline()
print(line1,type(line1))

line2=f.readline()
print(line2,type(line2))

line3=f.readline()
print(line3,type(line3))

f.close()
'''
#4. using while loop
'''
f= open("04_multiline.txt")
line= f.readline()
while(line!=""):
    print(line,end="")
    line=f.readline()

f.close()
'''

#5. append.py
'''
st="hey name how are you ..."
f=open("03_myfile.txt","a")# abb a sai append ho gaya abb jitnai barr mai eskoo chalunga 
f.write(st)             # yai utnai barr add hota rahaiga 
f.close()
'''


# with statement(the above program 1. is done but the task to f.close() therefore with )

with open("02_filetxt.txt") as f:
    print(f.read())# not need to close the file 


