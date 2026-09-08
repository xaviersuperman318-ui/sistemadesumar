import tkinter as tk
from tkinter import Tk, Label, Button, Entry,Frame, messagebox, mainloop
ventana =tk.Tk()

ventana.title("Calculadora de Ventas")
ventana.geometry("500x500")
ventana.resizable(False, False)
def sali():
    ventana.destroy()
def entra():
    nomber= texto1.get()
    cave= clave.get()
    if nomber=="xavier" and cave=="122":
        messagebox.showinfo("correcto , correcto mesm") 
    else:
        messagebox.showinfo("Incorrecto")
    
    
#TITULO-PRINCIPAL
#--------------------------
titulo=tk.Label(ventana, text="Seccion de inicio",
                font=("Arial",15,"bold"),
                fg="green"
                )
titulo.grid(row=0, column=0)
titulo.pack(padx=15)

#usuarios
tk.Label(ventana, text="usuario:", font=("Arial", 13 )).place(x=150, y=150)
texto1=tk.Entry(ventana, width=40)
texto1.place(x=220, y=150)

#clave
tk.Label(ventana, text="clave:",font=("arial",13 )).place(x=170, y=200)
clave=tk.Entry(ventana,width=40, show="*")
clave.place(x=220, y=200)

#botonentreda
btn1=tk.Button(ventana, text="Entra", command=entra)
btn1.place(x=200, y=250)

#btonsalir
btn2=tk.Button(ventana,text="Salir", command=sali)
btn2.place(x=260, y=250)




ventana.mainloop()