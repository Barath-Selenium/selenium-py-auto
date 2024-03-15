class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    @classmethod
    def from_single_argument(cls, arg):
        return cls(arg, None)

# Creating objects using different constructor methods
obj1 = MyClass(10, 20)
obj2 = MyClass.from_single_argument(30)
print(obj2.arg1)
print(obj2.arg2)
