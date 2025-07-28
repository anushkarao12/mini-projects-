import tkinter as tk
from tkinter import messagebox

def search_element():
    try:
        nums = list(map(int, entry_list.get().split()))
        target = int(entry_target.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers.")
        return

    for i in range(len(nums)):
        if nums[i] == target:
            result_label.config(text=f"Found at index {i}")
            return
    result_label.config(text="Not found")

# GUI Setup
root = tk.Tk()
root.title("Linear Search GUI")

tk.Label(root, text="Enter numbers (space-separated):").grid(row=0, column=0, padx=5, pady=5)
entry_list = tk.Entry(root, width=30)
entry_list.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Number to find:").grid(row=1, column=0, padx=5, pady=5)
entry_target = tk.Entry(root)
entry_target.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Search", command=search_element).grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
