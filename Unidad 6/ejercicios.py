

#%%
from tkinter import * 
ventana = Tk()
ventana.title("Ejercicio 1")
ventana.geometry("450x450")

var1 = StringVar()

mensaje1 = Message(ventana, 
                   textvariable=var1, 
                   relief=RAISED, 
                   justify=RIGHT, 
                   font='Helvetica 20')

var1.set("Hola Mundo")
mensaje1.pack()

ventana.mainloop()

# %%
from tkinter import *

def sel():
    texto = "Opción seleccionada: " + str(var.get())
    etiqueta1.config(text = texto)

ventana = Tk()
ventana.title("Ejercicio 2")
ventana.geometry("450x450")

etiqueta1 = Label(ventana, text = "Elige una opción")
etiqueta1.pack()

var = IntVar()

R1 = Radiobutton(ventana, text = "Opción 1",
                  variable = var,
                  value = 1, 
                  command = sel)
R1.pack( anchor = N) #qnchor = N, S, E, W (Norte, Sur, Este, Oeste) 

R2 = Radiobutton(ventana, text = "Opción 2",
                     variable = var,
                    value = 2, 
                    command = sel)
R2.pack( anchor = N)

R3 = Radiobutton(ventana, text = "Opción 3",
                        variable = var,
                        value = 3, 
                        command = sel)
R3.pack( anchor = N)

ventana.mainloop()

# %%
