class Employee:
    name = "Harry"
    language = "Py" #This is a class Attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(self):
        print("Good Morning")


harry = Employee()
harry.language = "Javascript" #This is an instance attribute
print(harry.language,harry.salary)
harry.getInfo()
#Employee.getInfo(harry)
