import math


class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return round(self.height * self.width, 2)
    # なぜ小数点以下2桁が表示されないのか

    def diagonal(self):
        dia = math.sqrt(self.height**2 + self.width**2)
        return round(dia, 2)

if __name__ == "__main__":
    rectangle1 = Rectangle(height=5, width=6)
    print(rectangle1.area())  # 30.00
    print(rectangle1.diagonal())  # 7.81

    rectangle2 = Rectangle(height=3, width=3)
    print(rectangle2.area())  # 9.00
    print(rectangle2.diagonal())  # 4.24