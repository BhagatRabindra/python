marks = {
#"Keys" : "value",
    "Harry" : "Coder", 
    "marks" : 100 , 
    "list" : [1,2,9]
}

# print(marks)
print(type(marks))

print(marks["list"])

print(marks.items())

#print to show the Keys and values seperatly 
print(marks.keys())
print(marks.values()) 

print(marks.update({"Rabindra":99}))

print(marks)

s1 = {1,5,90,45,3,7}
s2 = {4,6,9,45,36,7}

print(s1.union(s2))
print(s1.intersection(s2))

