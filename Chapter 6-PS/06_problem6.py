marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    grade = "Ex"
elif(marks<=90 and marks>=90):
    grade = "A"
elif(marks<=80 and marks>=90):
    grade = "B"
elif(marks<=70 and marks>=90):
    grade = "C"
elif(marks<=60 and marks>=90):
    grade = "D"
elif(marks<50):
    grade = "F"

print("Your grade is:",grade)