#Write a python function to print multiplication table of a given number

def table(num):
    i = 1
    while(i!=11):
        print(f"{num} X {i} is {num*i}")
        i+=1

num = int(input("Enter the number: "))

table(num)