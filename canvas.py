import numpy as np
from PIL import Image

class Canvas():
    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = colour

        # Generate the 3d array using numpy
        self.data = np.zeros((self.height, self.width, 3), dtype=np.np.uint8)
        # update the depth for color pixel array
        self.data[:] = self.colour

    def create_canvas(self, filename):
        img = Image.fromarray(self.data, 'RGB')
        img.save(filename)


my_canvas = Canvas(1000,1000, [188, 90, 35])
my_canvas.create_canvas('first_canvas')