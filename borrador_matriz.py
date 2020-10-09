import numpy as np
import tkinter as tk
from tkinter import ttk

        

#Crear instancia
win=tk.Tk()


#Agregar un titulo
win.title("CALCULADORA DE MATRICES")
win.geometry("500x300")
win.configure(background='dark turquoise')

var=tk.StringVar()
var1=tk.StringVar()



tk.Label(win, text="Matriz 1").grid(column=0, row=0)

A_1_1=tk.Entry(win,width=5)
A_1_1.grid(column=1, row=1)

A_1_2=tk.Entry(win,width=5)
A_1_2.grid(column=1, row=2)

A_2_1=tk.Entry(win,width=5)
A_2_1.grid(column=2, row=1)

A_2_2=tk.Entry(win,width=5)
A_2_2.grid(column=2, row=2)

tk.Label(win, text="Matriz 2").grid(column=3, row=0)

B_1_1=tk.Entry(win,width=5)
B_1_1.grid(column=4, row=1)

B_1_2=tk.Entry(win,width=5)
B_1_2.grid(column=4, row=2)

B_2_1=tk.Entry(win,width=5)
B_2_1.grid(column=5, row=1)

B_2_2=tk.Entry(win,width=5)
B_2_2.grid(column=5, row=2)

enter=ttk.Button(win,text="+", command=llenado_matrices)
enter.grid(column=11, row=2)

botonresta=ttk.Button(win,text="-", command=resta)
botonresta.grid(column=13, row=2)

botonmult=ttk.Button(win,text="*", command=mult)
botonmult.grid(column=15, row=2)

resultado=tk.Label(win, textvariable=var).grid(column=11, row=3)
resultado=tk.Label(win, textvariable=var1).grid(column=11, row=5)


win.mainloop()
