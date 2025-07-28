import subprocess
import tkinter as tk
from tkinter import ttk, messagebox


def fetch_wifi_passwords():
    try:
        data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

        wifi_info = []

        for profile in profiles:
            results = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode("utf-8").split("\n")
            password_lines = [line.split(":")[1][1:-1] for line in results if "Key Content" in line]
            password = password_lines[0] if password_lines else ""
            wifi_info.append((profile, password))

        return wifi_info

    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to retrieve Wi-Fi profiles.")
        return []


def display_wifi_passwords():
    wifi_list = fetch_wifi_passwords()

    for i in tree.get_children():
        tree.delete(i)

    for profile, password in wifi_list:
        tree.insert("", tk.END, values=(profile, password))


# Setup GUI
root = tk.Tk()
root.title("Wi-Fi Password Viewer")
root.geometry("500x400")

tk.Label(root, text="Saved Wi-Fi Profiles and Passwords", font=("Arial", 14)).pack(pady=10)

# Table (Treeview)
columns = ("SSID", "Password")
tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
tree.heading("SSID", text="Wi-Fi Name")
tree.heading("Password", text="Password")
tree.pack(pady=10, fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Button to load passwords
tk.Button(root, text="Show Passwords", command=display_wifi_passwords).pack(pady=10)

root.mainloop()
