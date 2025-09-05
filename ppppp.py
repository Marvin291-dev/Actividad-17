import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera calculadora")
ventana.geometry("300x325")

etiqueta = tk.Label(ventana, text="Ingrese el primer numero: ")
etiqueta.pack(pady = 5)

entrada1 = tk.Entry(ventana)
entrada1.pack(pady = 5)

entrada2 = tk.Entry(ventana)
entrada2.pack(pady = 5)

etiqueta2 = tk.Label(ventana, text="Resultado: ")
etiqueta2.pack(pady = 5)

def sumar():
    try:
        a = float(entrada1.get())
        b = float(entrada2.get())
        etiqueta2.config(text = f"El resultado es: {a + b}")
    except ValueError:
        etiqueta2.config(text = "Error ingresar numeros validos")

def restar():
    try:
        a = float(entrada1.get())
        b = float(entrada2.get())
        etiqueta2.config(text = f"El resultado es: {a - b}")
    except ValueError:
        etiqueta2.config(text = "Error ingresar numeros validos")

def multiplicar():
    try:
        a = float(entrada1.get())
        b = float(entrada2.get())
        etiqueta2.config(text = f"El resultado es: {a * b}")
    except ValueError:
        etiqueta2.config(text = "Error ingresar numeros validos")

def dividir():
    try:
        a = float(entrada1.get())
        b = float(entrada2.get())
        etiqueta2.config(text = f"El resultado es: {a / b}")
    except ValueError:
        etiqueta2.config(text = "Error ingresar numeros validos")

def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    etiqueta2.config(text = "Resultado: ")

boton_sumar = tk.Button(ventana, text = "Sumar", command = sumar, background= "lightblue", fg = "red")
boton_sumar.pack(pady = 5)
boton_sumar.place(x=85, y=127)

boton_restar = tk.Button(ventana, text = "Restar", command = restar)
boton_restar.pack(pady = 5)
boton_restar.place(x=190, y=127)

boton_multiplicar = tk.Button(ventana, text = "Multiplicar", command = multiplicar)
boton_multiplicar.pack(pady = 5)
boton_multiplicar.place(x=85, y=177)

boton_dividir = tk.Button(ventana, text = "Dividir", command = dividir)
boton_dividir.pack(pady = 5)
boton_dividir.place(x=190, y=177)

ventana.mainloop()