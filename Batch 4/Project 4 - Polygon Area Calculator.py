''' INFORMATION
In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle, and inherit its methods and attributes.

Rectangle class
When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:

set_width
set_height
get_area: Returns area (width * height)
get_perimeter: Returns perimeter (2 * width + 2 * height)
get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
get_picture: Returns a string that represents the shape using lines of '*'. The number of lines should be equal to the height and the number of '*' in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: 'Too big for picture.'.
get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
Additionally, if an instance of a Rectangle is represented as a string, it should look like: 'Rectangle(width=5, height=10)'.

Square class
The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The __init__ method should store the side length in both the width and height attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a set_side method. If an instance of a Square is represented as a string, it should look like: 'Square(side=9)'.

Additionally, the set_width and set_height methods on the Square class should set both the width and height.

'''


# Rectangle and Square classes with methods to calculate area, perimeter, diagonal, fit in times and picture representation.

# Solution by Javier Serrano Jodral

class Rectangle:
    def __init__(self, width, height):
        self.width:int = width
        self.height:int = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*self.width+2*self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):
        if self.width>50 or self.height>50:
            return 'Too big for picture.'
        output_string = ''
        for line in range(self.height):
            output_string += '*'*self.width + '\n'
        return output_string

    def get_amount_inside(self, other):
        return self.get_area() // other.get_area()

    def __str__(self):     # parametrize to make it valid for children classes
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'



class Square(Rectangle):
    
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, side):
        self.side = side
        

    def set_height(self, side):
        self.side = side

    def __str__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items() if key=='side']
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'



rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

print(Square(5))