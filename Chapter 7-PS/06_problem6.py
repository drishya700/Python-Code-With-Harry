# Write a program to calculate the factorial of a given number using for loop.

# 5! = 1*2*3*4*5
factorial = 1
n = int(input("Enter number: "))
for i in range(1, n+1):
    factorial*=i

print(f"The factorial of {n} is {factorial}")