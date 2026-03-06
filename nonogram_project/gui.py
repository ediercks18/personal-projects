import tkinter as tk

root = tk.Tk()
root.title("nonogram")
root.geometry("500x500")

# =============================================================================
# Make sure that all functions pass event as an argument
# and that all .binds do not have () at the end!!!!
# =============================================================================

def click(button):
    if button.cget("bg") == "white":
        button.config(bg="black")
    else:
        button.config(bg="white")

sidebar = tk.Frame(root, width=150, height=400, bg="skyblue")
sidebar.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.Y)

nonogram = tk.Frame(root, width=400, height=400, bg= "red")
nonogram.pack(padx=5, pady=5, side=tk.RIGHT)


for x in range(5):
    for y in range(10): 
        # For whatever reason on startup the button is pressed so you have to set
        # the color to the opposite color you have currently selected (e.g. white) 
        grid_square = tk.Button(nonogram, bg="black")
        grid_square.grid(row=x, column=y)
        grid_square.bind("<Button>", click(grid_square))
        grid_square["command"] = lambda grid_square = grid_square: click(grid_square)

for x in range(5):
    tk.Grid.rowconfigure(nonogram, x, weight=1)
for y in range(10):
    tk.Grid.columnconfigure(nonogram, y, weight=1)

root.mainloop()