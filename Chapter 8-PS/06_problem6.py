# Write a python function which converts inches to cms.

def in_to_cm(inch):
    return inch*2.54

inch = int(input("Enter the Length in Inches: "))

print(f"{inch} inches is {in_to_cm(inch)} cm")