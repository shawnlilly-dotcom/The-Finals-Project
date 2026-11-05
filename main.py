import tkinter as tk
from tkinter import messagebox, ttk
from database import add_game, create_database, get_games

create_database()

BG = "#20232A"
PANEL = "#2C313C"
TEXT = "#FFFFFF"

root = tk.Tk()
root.title("GameVault - Video Game Collection Manager")
root.geometry("900x650")
root.minsize(700, 540)
root.configure(bg=BG)

tk.Label(root, text="GameVault", font=("Arial", 28, "bold"), bg=BG, fg=TEXT).pack(pady=(20, 3))
tk.Label(root, text="Personal Video Game Collection Manager", font=("Arial", 12), bg=BG, fg="#BBBBBB").pack()

panel = tk.Frame(root, bg=PANEL)
panel.pack(padx=25, pady=20, fill="both", expand=True)

tk.Label(panel, text="Add a Game", font=("Arial", 18, "bold"), bg=PANEL, fg=TEXT).pack(pady=(15, 10))

form = tk.Frame(panel, bg=PANEL)
form.pack(fill="x", padx=20)


def form_label(text, row, column):
    tk.Label(form, text=text, bg=PANEL, fg=TEXT, anchor="w").grid(
        row=row, column=column, sticky="w", padx=8, pady=(6, 2)
    )


form.columnconfigure(0, weight=1)
form.columnconfigure(1, weight=1)
form_label("Title", 0, 0)
form_label("Genre", 0, 1)
title_entry = ttk.Entry(form)
title_entry.grid(row=1, column=0, sticky="ew", padx=8)
genre_entry = ttk.Entry(form)
genre_entry.grid(row=1, column=1, sticky="ew", padx=8)

form_label("Platform", 2, 0)
form_label("Completion Status", 2, 1)
platform_entry = ttk.Entry(form)
platform_entry.grid(row=3, column=0, sticky="ew", padx=8)
status_combo = ttk.Combobox(
    form, values=["Not Started", "In Progress", "Completed"], state="readonly"
)
status_combo.set("Not Started")
status_combo.grid(row=3, column=1, sticky="ew", padx=8)


def refresh_games():
    for item in game_table.get_children():
        game_table.delete(item)
    for game in get_games():
        game_table.insert("", "end", values=game)


def save_game():
    title = title_entry.get().strip()
    genre = genre_entry.get().strip()
    platform = platform_entry.get().strip()
    status = status_combo.get()
    if not title:
        messagebox.showwarning("Missing Title", "Please enter a game title.")
        title_entry.focus_set()
        return
    try:
        add_game(title, genre, platform, status)
        refresh_games()
    except Exception as error:
        messagebox.showerror("Database Error", f"Could not save game: {error}")
        return
    title_entry.delete(0, tk.END)
    genre_entry.delete(0, tk.END)
    platform_entry.delete(0, tk.END)
    status_combo.set("Not Started")
    title_entry.focus_set()
    messagebox.showinfo("Saved", f"{title} was added to your collection.")


ttk.Button(panel, text="Add Game", command=save_game).pack(pady=15)

tk.Label(panel, text="My Game Collection", font=("Arial", 16, "bold"), bg=PANEL, fg=TEXT).pack(pady=(4, 8))

table_frame = tk.Frame(panel, bg=PANEL)
table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
columns = ("ID", "Title", "Genre", "Platform", "Status")
game_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=9)
for col in columns:
    game_table.heading(col, text=col)
    game_table.column(col, width=65 if col == "ID" else 145, stretch=(col != "ID"))
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=game_table.yview)
game_table.configure(yscrollcommand=scrollbar.set)
game_table.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

refresh_games()
title_entry.focus_set()
root.mainloop()
