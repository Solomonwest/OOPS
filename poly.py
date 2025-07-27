class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

# Standalone function (not inside any class)
def lets_fly(flyer):
    flyer.fly()  # <- This line just says: "call .fly() on whatever 'flyer' is"

b = Bird()
a = Airplane()
c = "Not a flyer"

lets_fly(a)  # Output: Bird is flying