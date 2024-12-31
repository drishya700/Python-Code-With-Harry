# Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

def star(n):
    if(n==0):
        return #return means the function has concluded and the it will not execute further
    print("*"*n)
    star(n-1)

n = int(input("Enter the value of n: "))

print(star(n))