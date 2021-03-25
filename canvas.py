import numpy as np
from PIL import Image
from colour import Color




class Canvas:
    def __init__(self, height, width, colour):
        colours_rgb = list(Color(colour).rgb)
        for i in range(len(colours_rgb)):
            colours_rgb[i] = round(colours_rgb[i] * 255)
        self.width = width
        self.height = height
        self.colour = colours_rgb
        # Generate the 3d array using numpy
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # update the depth for color pixel array
        self.data[:] = self.colour

    def create_canvas(self, filename):
        img = Image.fromarray(self.data, 'RGB')
        img.save(filename)



