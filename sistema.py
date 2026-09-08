
import tkinter as tk
ventana = tk.Tk()

ventana.title("Calculadora de Ventas")
ventana.geometry("500x500")
ventana.resizable(False, False)

def suma():
    n1=texto1.get()
    n2= texto2.get()
    sumar=float(n1)+ float(n2)
    texto3.delete(0, tk.END)
    texto3.insert(0, f"{sumar:.2f}")    
  
def resta():
    n1=texto1.get()
    n2=texto2.get()
    resta= float(n1)-float(n2)
    texto3.delete(0,tk.END)
    texto3.insert(0,f"{resta:.2f}")
    
def borrar():
    texto1.delete(0, tk.END)
    texto2.delete(0, tk.END)
    texto3.delete(0, tk.END)
def salir():
    ventana.destroy()
#textos
texto=tk.Label(ventana,
        text="Sumar",
        font=("Arial", 15, "bold")
        )
texto.grid(row=0, column=0)
texto.pack(pady=15)

tk.Label(ventana, text="Ingresa el nùmero:").place(x=150, y=150)

texto1 = tk.Entry(ventana, bg="pink", width=30)
texto1.place(x=150, y=170)


tk.Label(ventana,text="Ingresa le nùmero:").place(x=150, y=220)
texto2=tk.Entry(ventana, bg="pink", width=30)
texto2.place(x=150 , y=250)

tk.Label(ventana, text="Resultado:", ).place(x=150, y=290)
texto3=tk.Entry(ventana , width=30)
texto3.place(x=150, y=310)

#Botondesuma
btn=tk.Button(ventana, text="Sumar ", command=suma , bg="blue")
btn.place(x=150 , y=350)
#botoderesta
btn2=tk.Button(ventana, text="Resta", bg="red", command=resta)
btn2.place(x=250, y=350 )

btn3=tk.Button(ventana, text="Borrar", command=borrar)
btn3.place(x=300, y=350)

btn3=tk.Button(ventana, text="Salir", command=salir)
btn3.place(x=350, y=350)
ventana.mainloop()