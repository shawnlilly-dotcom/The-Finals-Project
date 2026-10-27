
import tkinter as tk
from tkinter import ttk
from database import create_database

# Initialize database
create_database()

# Main window
root = tk.Tk()
root.title("GameVault - Video Game Collection Manager")
root.geometry("850x550")
root.configure(bg="#20232A")

# Title
title = tk.Label(
    root,
    text="GameVault",
    font=("Arial", 28, "bold"),
    bg="#20232A",
    fg="white"
)
title.pack(pady=25)

subtitle = tk.Label(
    root,
    text="Personal Video Game Collection Manager",
    font=("Arial", 13),
    bg="#20232A",
    fg="#BBBBBB"
)
subtitle.pack(pady=5)

# Main content area
frame = tk.Frame(root, bg="#2C313C")
frame.pack(padx=30, pady=25, fill="both", expand=True)

welcome = tk.Label(
    frame,
    text="Welcome to GameVault!",
    font=("Arial", 20, "bold"),
    bg="#2C313C",
    fg="white"
)
welcome.pack(pady=25)

description = tk.Label(
    frame,
    text="Manage and organize your video game collection.",
    font=("Arial", 12),
    bg="#2C313C",
    fg="white"
)
description.pack(pady=10)

# Sprint 1 database status
status = tk.Label(
    frame,
    text="Database initialized successfully.",
    font=("Arial", 11),
    bg="#2C313C",
    fg="#80D080"
)
status.pack(pady=15)

root.mainloop()
