# Write a program to find the sum of first n natural numbers using while loop

n = int(input("Enter n: "))

i = 1
sum = 0
while(i<=n):
    sum+=i
    i+=1

print(f"The sum of first {n} natural numbers is: {sum}")
