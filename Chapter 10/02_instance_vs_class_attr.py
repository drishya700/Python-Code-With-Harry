class Employee:
    name = "Harry"
    language = "Py" #This is a class Attribute
    salary = 1200000


harry = Employee()
harry.language = "Javascript" #This is an instance attribute
print(harry.language,harry.salary)

