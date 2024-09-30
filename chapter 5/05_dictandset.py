'''
marks={
    "harry" : 54,
    "sumit" : 93,
    "ram" : 98,
    
}
print(marks,type(marks))
print(marks["ram"])
# methods in dictonary
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"harry":90})
print(marks.get("sumit"))
'''


# set ....,.,.,.,.,.,.
s={4,6,3,7,8,43,4}
emptyset=set()
print(type(s),type(emptyset))
print(s)
# methods in sets
s.add(93)
print(s)
