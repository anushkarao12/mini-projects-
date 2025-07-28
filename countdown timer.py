import time
import tkinter as tk
from tkinter import messagebox

def start_timer():
    try:
        t = int(entry.get())
        countdown(t)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def countdown(t):
    if t >= 0:
        mins, secs = divmod(t, 60)
        timer_text = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timer_text)
        root.after(1000, countdown, t - 1)
    else:
        label.config(text="00:00")
        messagebox.showinfo("Time's Up", "⏰ Timer completed!")

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x200")
root.resizable(False, False)

# Create UI elements
tk.Label(root, text="Enter time (seconds):", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), justify='center')
entry.pack(pady=5)

tk.Button(root, text="Start Timer", font=("Arial", 12), command=start_timer).pack(pady=10)

label = tk.Label(root, text="00:00", font=("Arial", 30), fg="blue")
label.pack(pady=20)

# Run the application
root.mainloop()
