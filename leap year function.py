import tkinter as tk
from tkinter import messagebox

def is_leap(year):
    leap = False
    if (year % 4) == 0:
        leap = True
        if (year % 100) == 0:
            leap = False
            if (year % 400) == 0:
                leap = True
    return leap

def check_leap_year():
    year_str = entry.get()
    if not year_str.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid year.")
        return
    
    year = int(year_str)
    if is_leap(year):
        result_label.config(text=f"{year} is a Leap Year ✅")
    else:
        result_label.config(text=f"{year} is Not a Leap Year ❌")

# GUI setup
root = tk.Tk()
root.title("Leap Year Checker")
root.geometry("350x200")
root.resizable(False, False)

tk.Label(root, text="Enter Year:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=20, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Check", command=check_leap_year, font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
