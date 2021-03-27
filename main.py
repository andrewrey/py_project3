from canvas import Canvas
from square import Square
from rectangle import Rectangle
from fileshare import FileSharer

canvas_width = int(input("Enter the width for you canvas: "))
canvas_height = int(input("Enter the height of your canvas: "))
canvas_colour = input("Enter the colour you want for Canvas: ")
my_canvas = Canvas(height=canvas_height, width=canvas_width, colour=canvas_colour)

while True:
    user_choice = input(
        'Would you like to draw a "Square" or "Rectangle"? Type quit if you would like to leave!').lower()
    if user_choice == "square":
        x_value = int(input('Enter x value for start point  '))
        y_value = int(input('Enter y value for starting point '))
        side_value = int(input('Enter length of sides '))
        user_colour = input('Enter your square colour ')
        user_square = Square(x=x_value, y=y_value, side=side_value, colour=user_colour)
        user_square.draw_square(my_canvas)
    elif user_choice == 'rectangle':
        x_value = int(input('Enter x value for start point  '))
        y_value = int(input('Enter y value for starting point '))
        length_value = int(input('Enter the length of rectangle '))
        width_value = int(input('Enter the width of rectangle '))
        user_colour = input('Enter your rectangle colour ')
        user_rectangle = Rectangle(x=x_value, y=y_value, length=length_value, width=width_value, colour=user_colour)
        user_rectangle.draw_rectangle(my_canvas)
    else:
        user_file_name = input("Please provide a filename ")
        break

# first_square = Square(x=0, y=50, side=500, colour=[30, 55, 90])
# first_square.draw_square(my_canvas)
# first_rectangle = Rectangle(x=0, y=50, length=500, width=50, color=[200, 150, 66])
# first_rectangle.draw_rectangle(my_canvas)
my_canvas.create_canvas(f'{user_file_name}.png')
shared_png = FileSharer(filepath=f'{user_file_name}.png')
print(shared_png.upload())

