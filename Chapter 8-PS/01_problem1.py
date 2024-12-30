# Write a program using functions to find greatest of three numbers. 

def greatest(first, second, third):
    if(first>second and first>third):
        print(f"{first} is the greatest among the three")
    elif(second>first and second>third):
        print(f"{second} is the greatest among the three")
    elif(third>first and third>second):
        print(f"{third} is the greatest among the three")
    else:
        print("Invalid Input")

a = int(input("Enter Number: "))
b = int(input("Enter Number: "))
c = int(input("Enter Number: "))

greatest(a,b,c)