import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("300x300")

etiqueta = tk.Label(ventana, text="Ingrese el primer numero:")
etiqueta.pack(pady = 5)

entrada1 = tk.Entry(ventana)
entrada1.pack(pady = 5)

etiqueta2 = tk.Label(ventana, text="Ingrese el segundo numero:")
etiqueta2.pack(pady = 5)

entrada2 = tk.Entry(ventana)
entrada2.pack(pady = 5)

etiqueta3 = tk.Label(ventana, text=":")

def sumar():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    result = a + b
    print(f"El resultado es: {result}")

def restar():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    result = a - b
    print(f"El resultado es: {result}")

def multiplicar():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    result = a * b
    print(f"El resultado es: {result}")

def dividir():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    result = a / b
    print(f"El resultado es: {result}")

def limpiar():
    entrada1.delete(0, tk.END)
    etiqueta.config(text="Escribe el numero:")

    entrada2.delete(0, tk.END)
    etiqueta2.config(text="Ingrese el segundo numero:")

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady = 5)

boton_restar = tk.Button(ventana, text="Restar", command=restar)
boton_restar.pack(pady = 5)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multiplicar.pack(pady = 5)

boton_dividir = tk.Button(ventana, text="Dividir", command=dividir)
boton_dividir.pack(pady = 5)

ventana.mainloop()