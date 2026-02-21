import tkinter as tk

root = tk.Tk()
root.title("nonogram")
root.geometry("500x500")

# =============================================================================
# Make sure that all functions pass event as an argument
# and that all .binds do not have () at the end!!!!
# =============================================================================

def click(button):
    if button["bg"] == "white":
        button["bg"] = "black"
    else:
        button["bg"] = "white"

sidebar = tk.Frame(root, width=150, height=400, bg="skyblue")
sidebar.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.Y)

nonogram = tk.Frame(root, width=400, height=400, bg= "red")
nonogram.pack(padx=5, pady=5, side=tk.RIGHT)


for x in range(5):
    for y in range(10): 
        grid_square = tk.Button(nonogram, bg="white")
        grid_square.grid(row=x, column=y)
        grid_square.bind("<Button>", click)
        grid_square["command"] = lambda grid_square = grid_square: click(grid_square)

for x in range(5):
    tk.Grid.rowconfigure(nonogram, x, weight=1)
for y in range(10):
    tk.Grid.columnconfigure(nonogram, y, weight=1)

root.mainloop()