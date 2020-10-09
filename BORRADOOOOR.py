import numpy as np
import tkinter as tk
from tkinter import ttk

n=2
m=2


A=np.zeros((n,m))
B=np.zeros((n,m))
C=np.zeros((n,m))

def llenado_matrices():
    for i in range(1,n):
        for j in range(1,m):
            A[i,j]="A_"+ str(i).get() + "_" + str(j).get()
            return var.set(A[i,j])
        
#Crear instancia
win=tk.Tk()


#Agregar un titulo
win.title("CALCULADORA DE MATRICES")
win.geometry("500x300")
win.configure(background='dark turquoise')

var=tk.StringVar()




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

enter=ttk.Button(win,text="Imprimir resultado", command=llenado_matrices)
enter.grid(column=11, row=2)


resultado=tk.Label(win, textvariable=var).grid(column=11, row=3)


A1=llenado_matrices()
print (str(int (A1)))

win.mainloop()
