class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False

r1 = Rectangle(5, 3)
r2 = Rectangle(4, 4)

print(r1.area())
print(r1.perimeter())
print(r1.is_square())
print(r2.is_square())