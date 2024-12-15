#Write a program to find whether a given number is prime or not.

num = int(input("Enter Number: "))

if num > 1:
    isPrime = True
    for i in range(2, int(num//2) + 1):  # Check only up to the square root of the number
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        print("The number is Prime")
    else:
        print("The number is not Prime")
else:
    print("The number is not Prime")

