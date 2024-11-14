marks1 = int(input("Enter the marks in Maths: "))
marks2 = int(input("Enter the marks in English: "))
marks3 = int(input("Enter the marks in SST: "))

#Check for total percentage
total_percentage = ((marks1+marks2+marks3)/3)

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass")

else:
    print("You failed, Try again next year!")