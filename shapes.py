class Shape():
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

class Rectangle(Shape):
    def __init__(self, x_pos, y_pos, width, height):
        super().__init__(x_pos, y_pos)
        self.width = width
        self.height = height

    def get_points(self):
        return [(self.x_pos, self.y_pos), 
                (self.x_pos + self.width, self.y_pos), 
                (self.x_pos + self.width, self.y_pos + self.height), 
                (self.x_pos, self.y_pos + self.height)]

class Square(Rectangle):
    def __init__(self, x_pos, y_pos, size):
        super().__init__(x_pos, y_pos, size, size)

rect1 = Rectangle(0, 0, 10, 20)
print(rect1.get_points())

square1 = Square(0, 0, 40)
print(square1.get_points())

# TODOs:
# Add a colour attribute as a string which can be set, but is default to "white"
# Add a get_area() method so each Square and Rectangle work
# Add a scale_up() method which takes a multiplier (e.g. 2 doubles the size)
# Harder: Add an EquilateralTriangle Class where size is the length if all sides
# Much harder: Add a Triange Class with side_a, side_b, side_c, then calculate the points.
