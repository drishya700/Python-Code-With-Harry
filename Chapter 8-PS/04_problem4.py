#. Write a recursive function to calculate the sum of first n natural numbers.

def first_N(n):
    if(n==0 or n==1):
        return 1
    return n + first_N(n-1)

n = int(input("Enter the value of N: "))

print(f"The sum of first {n} natural numbers is {first_N(n)}")

