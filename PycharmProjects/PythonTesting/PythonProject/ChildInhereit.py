from OopsDemo import Calculator


class ChildInherit(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 2)

    def get_methods_from_parent(self):
        return self.num + self.num2 + self.summation()


obj = ChildInherit()
print(obj.get_methods_from_parent())







