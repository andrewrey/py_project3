from colour import Color


class Square:
    def __init__(self, x, y, side, colour):
        colours_rgb = list(Color(colour).rgb)
        for i in range(len(colours_rgb)):
            colours_rgb[i] = round(colours_rgb[i] * 255)
        self.x = x
        self.y = y
        self.side = side
        self.colour = colours_rgb

    def draw_square(self, canvas):
        canvas.data[self.y:self.y + self.side, self.x:self.x + self.side] = self.colour
