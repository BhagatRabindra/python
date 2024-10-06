#list1 = [1,2,3,2,1]
list1 = ["M","A","A","M"]
list2 = [1,2,3,4]

copy1 = list1.copy()
copy1.reverse()

copy2 = list2.copy()
copy2.reverse()

if(copy1 == list1):
    print("Copy 1 is Palindrome")
else :
    print("Copy 1 is Not Palindrame")

if(copy2 == list1):
    print("Copy 2 is Palindrome")
else:
    print("Copy 2 is Not palindrome")
