import tkinter as tk
from tkinter import colorchooser
import turtle
import threading

def draw_shape(shape, size, color, repetitions, bg_color, speed):
    window = turtle.Screen()
    window.bgcolor(bg_color)
    nate = turtle.Turtle()
    nate.shape("turtle")
    nate.color(color)
    nate.speed(speed)

    if shape == "Square":
        for _ in range(repetitions):
            for _ in range(4):
                nate.forward(size)
                nate.right(90)
            nate.right(10)

    elif shape == "Line":
        nate.forward(size)

    elif shape == "Triangle":
        for _ in range(3):
            nate.forward(size)
            nate.left(120)


    elif shape == "Star Squares":
        for _ in range(repetitions):
            for _ in range(4):
                nate.forward(size)
                nate.right(90)
            nate.right(160)

    window.exitonclick()

def start_drawing():
    shape = shape_var.get()
    try:
        size = int(size_entry.get())
        reps = int(rep_entry.get())
        speed = int(speed_entry.get())
    except ValueError:
        return
    color = color_display["bg"]
    bg_color = bg_display["bg"]
    threading.Thread(target=draw_shape, args=(shape, size, color, reps, bg_color, speed)).start()

def choose_color():
    color_code = colorchooser.askcolor(title="Choose Turtle Color")
    if color_code:
        color_display.config(bg=color_code[1])

def choose_bg_color():
    color_code = colorchooser.askcolor(title="Choose Background Color")
    if color_code:
        bg_display.config(bg=color_code[1])

# GUI Setup
root = tk.Tk()
root.title("Turtle Drawing GUI")

tk.Label(root, text="Shape:").grid(row=0, column=0, padx=5, pady=5)
shape_var = tk.StringVar(value="Square")
shape_menu = tk.OptionMenu(root, shape_var, "Square", "Line", "Triangle", "Star Squares")
shape_menu.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Size:").grid(row=1, column=0, padx=5, pady=5)
size_entry = tk.Entry(root)
size_entry.grid(row=1, column=1, padx=5, pady=5)
size_entry.insert(0, "100")

tk.Label(root, text="Repetitions:").grid(row=2, column=0, padx=5, pady=5)
rep_entry = tk.Entry(root)
rep_entry.grid(row=2, column=1, padx=5, pady=5)
rep_entry.insert(0, "36")

tk.Label(root, text="Color:").grid(row=3, column=0, padx=5, pady=5)
color_display = tk.Label(root, bg="white", width=10)
color_display.grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="Choose Color", command=choose_color).grid(row=3, column=2, padx=5, pady=5)

tk.Label(root, text="Background:").grid(row=4, column=0, padx=5, pady=5)
bg_display = tk.Label(root, bg="black", width=10)
bg_display.grid(row=4, column=1, padx=5, pady=5)
tk.Button(root, text="Choose Background", command=choose_bg_color).grid(row=4, column=2, padx=5, pady=5)

tk.Label(root, text="Speed (1-10):").grid(row=5, column=0, padx=5, pady=5)
speed_entry = tk.Entry(root)
speed_entry.grid(row=5, column=1, padx=5, pady=5)
speed_entry.insert(0, "5")

tk.Button(root, text="Draw", command=start_drawing).grid(row=6, column=0, columnspan=3, pady=10)

root.mainloop()
