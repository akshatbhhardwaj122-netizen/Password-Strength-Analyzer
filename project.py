import tkinter as tk
from tkinter import ttk
import re

def check_strength(*args):
    password = password_var.get()
    strength = 0
    remarks = ""
    color = "#E74C3C"  # Default Red

    if len(password) == 0:
        strength_label.config(text="", bg="#F0F0F0")
        progress['value'] = 0
        return

    # Strength Logic
    if len(password) >= 8: strength += 1
    if re.search("[a-z]", password) and re.search("[A-Z]", password): strength += 1
    if re.search("[0-9]", password): strength += 1
    if re.search("[!@#$%^&*(),.?\":{}|<> ]", password): strength += 1

    # Mapping Strength to UI
    if strength == 1:
        remarks, color = "Weak", "#E74C3C"
    elif strength == 2:
        remarks, color = "Fair", "#F1C40F"
    elif strength == 3:
        remarks, color = "Good", "#3498DB"
    elif strength == 4:
        remarks, color = "Strong", "#2ECC71"

    progress['value'] = (strength / 4) * 100
    strength_label.config(text=f"Strength: {remarks}", fg=color)

# Root window setup
root = tk.Tk()
root.title("ShieldPass Analyzer")
root.geometry("400x250")
root.configure(padx=20, pady=20)

# UI Elements
title_label = tk.Label(root, text="Password Strength Analyzer", font=("Helvetica", 14, "bold"))
title_label.pack(pady=(0, 10))

password_var = tk.StringVar()
password_var.trace_add("write", check_strength)

entry = tk.Entry(root, textvariable=password_var, show="*", font=("Helvetica", 12), width=30)
entry.pack(pady=10)

# Progress Bar (The "Meter")
style = ttk.Style()
style.theme_use('default')
style.configure("TProgressbar", thickness=10)
progress = ttk.Progressbar(root, orient="horizontal", length=250, mode="determinate", style="TProgressbar")
progress.pack(pady=10)

strength_label = tk.Label(root, text="", font=("Helvetica", 11, "bold"))
strength_label.pack()

root.mainloop()