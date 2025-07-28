import tkinter as tk
from tkinter import messagebox

# Morse code symbols dictionary
symbols = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
    "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
    " ": "/"  # Optional: Use '/' for space between words
}

def convert_to_morse():
    text = entry.get().lower()
    if not text.strip():
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    output = [symbols.get(char, '') for char in text if char in symbols]
    morse_code = ' '.join(output)
    result_label.config(text=f"Morse Code:\n{morse_code}")
    copy_button.config(state="normal")

def copy_to_clipboard():
    morse_text = result_label.cget("text").replace("Morse Code:\n", "")
    root.clipboard_clear()
    root.clipboard_append(morse_text)
    messagebox.showinfo("Copied", "Morse code copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Text to Morse Code Converter")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Convert", command=convert_to_morse, font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=380, justify="left")
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy Morse Code", command=copy_to_clipboard, font=("Arial", 12))
copy_button.pack(pady=5)
copy_button.config(state="disabled")

root.mainloop()
