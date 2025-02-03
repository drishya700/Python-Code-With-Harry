# Add a static method in problem 2, to greet the user with hello
class Calculator:
    def __init__(self,number):
        self.number = number

    def square(self):
        print(f"The square of {self.number} is {self.number*self.number}")

    def cube(self):
        print(f"The cube of {self.number} is {self.number*self.number*self.number}")

    def squareroot(self):
        print(f"The square root of {self.number} is {self.number**1/2}")

    @staticmethod
    def hello():
        print("Hello There!")

a = Calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()