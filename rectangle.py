class Rectangle:
    def __init__(self, x, y, length, width, color):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.color = color

    def draw_rectangle(self, canvas):
        canvas.data[self.y:self.y + self.length, self.x:self.x + self.width] = self.color


