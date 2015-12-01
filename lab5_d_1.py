from Tkinter import *
import random
from lab4_b import random_color, random_size

# Graphics commands.
handlers = []
color = ''
global_canvas = ''


def draw_circle(canvas, color, size, position):
    """

    :param canvas:
    :param color:
    :param size:
    :param position:
    :return handle:

    Takes a Tkinter canvas, a color string, an integer size, and a tuple of
    x,y coordinates for the center of the rectangle that bounds the circle.

    Returns the handle from the created circle.
    """
    upper_x = position[0] - size / 2
    upper_y = position[1] - size / 2

    lower_x = position[0] + size / 2
    lower_y = position[1] + size / 2

    return canvas.create_oval(
        upper_x, upper_y, lower_x, lower_y, fill=color, outline=color
    )

# Event handlers.


def key_handler(event):
    '''Handle key presses.'''
    # <your code goes here>
    if event.keysym == 'q':
        quit()
    elif event.keysym == 'c':
        global color
        color = random_color()
    elif event.keysym == 'x':
        global handlers
        global global_canvas
        for index, handler in enumerate(list(handlers)):
            global_canvas.delete(handler)
            del handlers[index]


def button_handler(event):
    '''Handle left mouse button click events.'''
    global global_canvas
    global handlers
    handlers.append(
        draw_circle(
            global_canvas,
            color,
            random_size(10, 50),
            (event.x, event.y)
        )
    )


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    global_canvas = canvas
    color = random_color()

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()
