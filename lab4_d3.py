import lab4_b
import Tkinter
from lab4_d2 import draw_square


if __name__ == '__main__':
    root = Tkinter.Tk()
    root.geometry('800x800')

    c = Tkinter.Canvas(root, width=800, height=800)
    c.pack()

    for i in range(50):
        draw_square(c,
                    lab4_b.random_color(),
                    lab4_b.random_size(20, 150),
                    lab4_b.random_position(800, 800))

    root.bind("q", quit)
    root.mainloop()

