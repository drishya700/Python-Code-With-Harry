# Use comparison operator to find out whether ‘a’ given variable a is greater than
# ‘b’ or not. Take a = 34 and b = 80

first = int(input("Enter First Number: "))

second = int(input("Enter Second Number: "))

if(first<second):
    print("Second is greater than the first number")

elif(second<first):
    print("First is greater than the second number")

elif(first==second):
    print("Equal Values")

else:
    print("Invalid Input")