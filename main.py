from canvas import Canvas
from square import Square
from rectangle import Rectangle

canvas_width = int(input("Enter the width for you canvas: "))
canvas_height = int(input("Enter the height of your canvas: "))
canvas_colour = input("Enter the colour you want for Canvas: ")


my_canvas = Canvas(height=canvas_height, width=canvas_width, colour=canvas_colour)
first_square = Square(0, 0, 500, [30, 55, 90])
first_square.draw_square(my_canvas)
first_rectangle = Rectangle(x=0, y=0, length=500, width=50, color=[200, 150, 66])
first_rectangle.draw_rectangle(my_canvas)
my_canvas.create_canvas('first_canvas.png')
print(my_canvas.colour)