import tkinter as tk

# Ventana
formulario = tk.Tk()
formulario.title("Formulario Básico")
formulario.geometry("400x300")


# Variables
nombre = tk.StringVar()
edad = tk.StringVar()
correo = tk.StringVar()

# Label y caja de texto 1
tk.Label(formulario, text="Nombre:").pack(pady=10)
tk.Entry(formulario, textvariable=nombre, width=40).pack(pady=5)

# Label y caja de texto 2
tk.Label(formulario, text="Edad:").pack(pady=10)
tk.Entry(formulario, textvariable=edad, width=40).pack(pady=5)

# Label y caja de texto 3
tk.Label(formulario, text="Correo:").pack(pady=10)
tk.Entry(formulario, textvariable=correo, width=40).pack(pady=5)

# Botón
tk.Button(formulario, text="Guardar", bg="blue", fg="white").pack(pady=20)

# Inicio de ventana
formulario.mainloop()