from colour import Color

class Rectangle:
    def __init__(self, x, y, length, width, colour):
        rgb_colour = list(Color(colour).rgb)
        for i in range(len(rgb_colour)):
            rgb_colour[i] = round(rgb_colour[i] * 255)
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.color = rgb_colour

    def draw_rectangle(self, canvas):
        canvas.data[self.y:self.y + self.length, self.x:self.x + self.width] = self.color


