import tkinter as tk

root = tk.Tk()
root.title("nonogram")
root.geometry("500x500")




# Create Sidebar

root.update()
sidebar = tk.Frame(root, width=100, bg="red", height= root.winfo_height())
sidebar.grid()
# Create Input for length/width to allow selection of nongram size

nrow = tk.IntVar()
nrow_input = tk.Entry(sidebar, textvariable=nrow)
nrow_input.grid(row=0, padx=5, pady=10)

ncol = tk.IntVar()
ncol_input = tk.Entry(sidebar, textvariable=ncol)
ncol_input.grid(row=1, padx=5, pady=10)

root.mainloop()