import numpy as np
from PIL import Image
from square import Square
from rectangle import Rectangle



class Canvas:
    def __init__(self, height, width, colour):
        self.width = width
        self.height = height
        self.colour = colour

        # Generate the 3d array using numpy
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # update the depth for color pixel array
        self.data[:] = self.colour

    def create_canvas(self, filename):
        img = Image.fromarray(self.data, 'RGB')
        img.save(filename)


my_canvas = Canvas(1000, 1000, [188, 90, 35])
first_square = Square(0, 0, 500, [30, 55, 90])
first_square.draw_square(my_canvas)
first_rectangle = Rectangle(x=0, y=0, length=500, width=50, color=[200, 150, 66])
first_rectangle.draw_rectangle(my_canvas)
my_canvas.create_canvas('first_canvas.png')
