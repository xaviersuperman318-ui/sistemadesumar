import tkinter as tk
from tkinter import messagebox


ventana = tk.Tk()

ventana.title("Calculadora de Ventas")
ventana.geometry("500x500")
ventana.resizable(False, False)


# -------------------------
# FUNCIONES
# -------------------------

def sali():
    ventana.destroy()


def entra():
    nombre = texto1.get()
    clave_ingresada = clave.get()

    if nombre == "xavier" and clave_ingresada == "122":
        messagebox.showinfo(
            "Correcto",
            "¡Usuario y clave correctos!"
        )
    else:
        messagebox.showerror(
            "Incorrecto",
            "Usuario o clave incorrectos"
        )


# -------------------------
# TITULO PRINCIPAL
# -------------------------

titulo = tk.Label(
    ventana,
    text="Sección de inicio",
    font=("Arial", 15, "bold"),
    fg="green"
)

titulo.pack(pady=15)


# -------------------------
# USUARIO
# -------------------------

tk.Label(
    ventana,
    text="Usuario:",
    font=("Arial", 13)
).place(x=150, y=150)

texto1 = tk.Entry(
    ventana,
    width=40
)

texto1.place(x=220, y=150)


# -------------------------
# CLAVE
# -------------------------

tk.Label(
    ventana,
    text="Clave:",
    font=("Arial", 13)
).place(x=170, y=200)

clave = tk.Entry(
    ventana,
    width=40,
    show="."
)

clave.place(x=220, y=200)


# -------------------------
# BOTÓN ENTRAR
# -------------------------

btn1 = tk.Button(
    ventana,
    text="Entrar",
    command=entra
)

btn1.place(x=200, y=250)


# -------------------------
# BOTÓN SALIR
# -------------------------

btn2 = tk.Button(
    ventana,
    text="Salir",
    command=sali
)

btn2.place(x=260, y=250)


# -------------------------
# EJECUTAR VENTANA
# -------------------------

ventana.mainloop()