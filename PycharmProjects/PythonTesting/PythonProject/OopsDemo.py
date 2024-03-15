class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b

    def get_calci(self):
        print("I am becoming death and destroyer of the world")

    def summation(self):
        return self.firstNumber + self.secondNumber + self.num


obj = Calculator(2, 3)
obj.get_calci()
print(obj.summation())

obj1 = Calculator(4, 3)
print(obj1.summation())










