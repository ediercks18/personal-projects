import tkinter as tk

root = tk.Tk()
root.title("nonogram")
root.geometry("500x500")

# =============================================================================
# Make sure that all functions pass event as an argument
# and that all .binds do not have () at the end!!!!
# =============================================================================
def test(event):
    print("hello world!")

# Create Sidebar

root.update()
sidebar = tk.Frame(root, width=300, bg="red", height= root.winfo_height())
sidebar.grid()

# Create Input for length/width to allow selection of nongram size

root.update()
sidebar.bind("<Button>", test)

nrow = tk.IntVar()
nrow_input = tk.Entry(sidebar, textvariable=nrow)
nrow_input.grid(row=0, padx=5, pady=10)

ncol = tk.IntVar()
ncol_input = tk.Entry(sidebar, textvariable=ncol)
ncol_input.grid(row=1, padx=5, pady=10)

root.mainloop()