a = int(input("Enter you age :"))

# if statement no. 1
if(a%2 ==0):
    print("a is even.")


# if elif else ladder 
if(a>18):
    print("You are above the age of consent.")
    print("Good for you.")

elif(a<0):
    print("You are entering invalid negative age.")

elif(a==0):
    print("You are entering 0 which is not valid age.")

else:
    print("You are below the age of consent.")

print("End of the program.")