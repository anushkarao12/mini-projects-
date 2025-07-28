import tkinter as tk
from tkinter import messagebox

# Selection Sort logic
def selectionSort(array):
    size = len(array)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        array[step], array[min_idx] = array[min_idx], array[step]
    return array

# Button click event handler
def perform_sort():
    input_data = entry.get()
    try:
        # Convert input string to list of integers
        data = list(map(int, input_data.split(',')))
        sorted_data = selectionSort(data.copy())
        result_label.config(text=f"Sorted Array: {sorted_data}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a list of integers separated by commas.")

# Create main window
root = tk.Tk()
root.title("Selection Sort GUI")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

# Title label
title = tk.Label(root, text="Selection Sort (Ascending Order)", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Input prompt
prompt = tk.Label(root, text="Enter numbers separated by commas:", bg="#f0f0f0")
prompt.pack()

# Input entry
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Sort button
sort_button = tk.Button(root, text="Sort", command=perform_sort, bg="#4CAF50", fg="white", width=10)
sort_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Courier New", 12))
result_label.pack()

# Start GUI loop
root.mainloop()
