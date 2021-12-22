# starting trial code

from tkinter import *


def circle(canvas, x, y, r):
    my_circle = canvas.create_oval(x - r, y - r, x + r, y + r)
    return my_circle


def line(canvas, x, y, h, w):
    my_line = canvas.create_line(x, y, h, w, fill="#476042")
    return my_line


def label(master, my_x, my_y, i):
    l = Label(master, text=str(i))
    l.config(font=("Courier", 16))
    l.place(x=my_x, y=my_y)


def solutions(master, w):
    label(master, 90, 90, 0)
    label(master, 90, 490, 1)
    label(master, 190, 290, 2)
    label(master, 490, 190, 3)
    label(master, 190, 540, 4)
    label(master, 390, 390, 5)
    label(master, 640, 340, 6)
    label(master, 690, 140, 7)
    circle(w, 100, 100, 30)
    circle(w, 100, 500, 30)
    circle(w, 200, 550, 30)
    circle(w, 200, 300, 30)
    circle(w, 400, 400, 30)
    circle(w, 650, 350, 30)
    circle(w, 700, 150, 30)
    circle(w, 500, 200, 30)
    return 0


def problem(master, w):
    label(master, 90, 90, 0)
    label(master, 90, 490, 1)
    label(master, 190, 290, 2)
    label(master, 490, 190, 3)
    label(master, 190, 540, 4)
    label(master, 390, 390, 5)
    label(master, 640, 340, 6)
    label(master, 690, 140, 7)
    circle(w, 100, 100, 30)
    circle(w, 100, 500, 30)
    circle(w, 200, 550, 30)
    circle(w, 200, 300, 30)
    circle(w, 400, 400, 30)
    circle(w, 650, 350, 30)
    circle(w, 700, 150, 30)
    circle(w, 500, 200, 30)
    line(w, 100, 100, 200, 300)
    line(w, 200, 300, 400, 400)
    line(w, 400, 400, 650, 350)
    line(w, 400, 400, 200, 550)
    line(w, 200, 550, 100, 500)
    line(w, 400, 400, 100, 500)
    line(w, 200, 300, 100, 500)
    line(w, 200, 300, 500, 200)
    line(w, 650, 350, 500, 200)
    line(w, 100, 100, 500, 200)
    line(w, 700, 150, 500, 200)
    line(w, 700, 150, 650, 350)
    line(w, 500, 200, 400, 400)
    return 0


def switch():
    pass


class GUI:
    my_button = True
    master = Tk()
    canvas_width = 800
    canvas_height = 600
    w = Canvas(master, width=canvas_width, height=canvas_height)
    w.pack()
    label(master, 100, 0, "Minimum Spanning Tree with Kruskal's algorithm")
    problem(master, w)
    # solutions (master, w)
    b = Button(master, text="Show solutions", command=switch())
    b.pack()

    mainloop()
