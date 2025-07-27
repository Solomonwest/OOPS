class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c  # This one **overwrites** the previous

calc = Calculator()

print(calc.add(2, 3))  # This will raise an error because the first add is overwritten