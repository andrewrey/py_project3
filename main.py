from canvas import Canvas
from square import Square
from rectangle import Rectangle



my_canvas = Canvas(1000, 1000, [22, 88, 220])
first_square = Square(0, 0, 500, [30, 55, 90])
first_square.draw_square(my_canvas)
first_rectangle = Rectangle(x=0, y=0, length=500, width=50, color=[200, 150, 66])
first_rectangle.draw_rectangle(my_canvas)
my_canvas.create_canvas('first_canvas.png')