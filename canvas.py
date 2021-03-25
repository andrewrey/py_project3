import numpy as np
from PIL import Image




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



