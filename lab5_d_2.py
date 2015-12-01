from Tkinter import *
import random, math
from lab4_b import random_color, random_size

# Graphics commands.
handlers = []
color = ''
global_canvas = ''
N = 5


def draw_line(canvas, color, starting_position, ending_position):
    """

    Args:
        canvas (Canvas):
        color (str):
        starting_position (Tuple[int, int]):
        ending_position  (Tuple[int, int]):

    Returns:

    """
    return canvas.create_line(
        starting_position[0],
        starting_position[1],
        ending_position[0],
        ending_position[1],
        fill=color,
    )


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


def draw_star(canvas, color, size, position):
    """

    Args:
        canvas (Canvas): Canvas object to draw on
        color (str): Hexadecimal color code
        size (int): Integer that represents the diameter of the star
        position (Tuple[int, int]): x,y coordinates of the center of a star

    Returns:

    """
    points = []
    angle = (2.0 * math.pi / N)
    line_handlers = []
    for i in range(N):
        points.append(
            (
                (size/2.0) * math.cos((angle * i) +
                                      (math.pi / 2.0)) + position[0],
                (size/2.0) * math.sin((angle * i) -
                                      (math.pi / 2.0)) + position[1]
            )
        )
    for index, point in enumerate(points):
        line_handlers.append(
            draw_line(canvas,
                      color,
                      point,
                      points[(index + (N - 1) / 2) % N]
                      )
        )
    return line_handlers

# Event handlers.


def key_handler(event):
    '''Handle key presses.'''
    global N
    if event.keysym == 'q':
        quit()
    elif event.keysym == 'c':
        global color
        color = random_color()
    elif event.keysym == 'x':
        global handlers
        global global_canvas
        for handler in list(handlers):
            global_canvas.delete(handler)
            handlers.remove(handler)
    elif event.keysym == 'minus':
        if (N - 2) >= 5:
            N -= 2
    elif event.keysym == 'plus':
        N += 2


def button_handler(event):
    '''Handle left mouse button click events.'''
    global global_canvas
    global handlers
    handlers += draw_star(
        global_canvas,
        color,
        random_size(50, 100),
        (event.x, event.y)
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
