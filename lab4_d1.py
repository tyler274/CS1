import Tkinter


root = Tkinter.Tk()
root.geometry('800x800')

c = Tkinter.Canvas(root, width=800, height=800)
c.pack()

c.create_rectangle(0, 0, 100, 100, fil='red', outline='red')
c.create_rectangle(700, 0, 800, 100, fil='green', outline='green')
c.create_rectangle(0, 700, 100, 800, fil='blue', outline='blue')
c.create_rectangle(700, 700, 800, 800, fil='yellow', outline='yellow')


root.mainloop()