import tkinter as tk

# Función para calcular IMC
def calcular_imc():
    try:
        peso = float(dato1.get())
        altura = float(dato2.get())

        imc = peso / (altura * altura)

        resultado.config(text=f"Tu IMC es: {round(imc,2)}")

    except:
        resultado.config(text="Ingresa datos válidos")


# Ventana
formulario = tk.Tk()
formulario.title("Calculadora IMC")
formulario.geometry("400x300")


# Variables
dato1 = tk.StringVar()
dato2 = tk.StringVar()


# Etiquetas y cajas de texto
tk.Label(formulario, text="Peso en kg:").pack(pady=10)
tk.Entry(formulario, textvariable=dato1, width=40).pack(pady=5)

tk.Label(formulario, text="Altura en metros:").pack(pady=10)
tk.Entry(formulario, textvariable=dato2, width=40).pack(pady=5)


# Botón
tk.Button(formulario,
          text="Calcular IMC",
          command=calcular_imc,
          bg="green",
          fg="white").pack(pady=20)


# Resultado
resultado = tk.Label(formulario, text="Resultado: ")
resultado.pack(pady=10)


# Inicio
formulario.mainloop()