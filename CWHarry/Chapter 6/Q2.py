marks1 = int(input("Enter marks1 :"))
marks2 = int(input("Enter marks2 :"))
marks3 = int(input("Enter marks3 :"))
marks4 = int(input("Enter marks4 :"))

total_percentage = (100* (marks1 + marks2 + marks3))/300

if(total_percentage >=40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
    print("You are passed: ", total_percentage)

else:
    print("You are failed , try45
          56
           26
             again next year:", total_percentage)
