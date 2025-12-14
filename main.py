from tkinter import *
from tkinter import ttk


def calculateBMI(*args):
    try:
        weight_value = float(weight.get())
        height_value = float(height.get())
        bmi.set(round(weight_value / (height_value * height_value), 3))
    except ValueError:
        pass


root = Tk()
root.title("bmi Calculator")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

weight = StringVar()
weight_input = ttk.Entry(mainframe, width=7, textvariable=weight)
weight_input.grid(column=2, row=1, sticky=(W, E))

height = StringVar()
height_input = ttk.Entry(mainframe, width=7, textvariable=height)
height_input.grid(column=2, row=2, sticky=(W, E))

bmi = StringVar()
ttk.Label(mainframe, textvariable=bmi).grid(column=2, row=4, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculateBMI).grid(
    column=3, row=4, sticky=W
)

ttk.Label(mainframe, text="weight").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="your BMI:").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="height").grid(column=3, row=2, sticky=W)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

weight_input.focus()
root.bind("<Return>", calculateBMI)

root.mainloop()
