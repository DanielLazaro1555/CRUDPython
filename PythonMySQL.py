# Importa el módulo tkinter y lo renombra como tk
import tkinter as tk

# Importa todas las clases y funciones de tkinter
from tkinter import *

# Importa el módulo ttk de tkinter, que proporciona widgets más modernos
from tkinter import ttk

# Importa la clase messagebox de tkinter, que se utiliza para mostrar mensajes emergentes
from tkinter import messagebox

# Define una clase llamada FormularioClientes


class FormularioClientes:
    # Define un método llamado Formulario dentro de la clase FormularioClientes
    def Formulario():
        try:
            # Crea una instancia de la clase Tk(), que representa la ventana principal de la aplicación
            base = tk.Tk()

            # Establece las dimensiones de la ventana principal
            base.geometry("1200x300")

            # Establece el título de la ventana principal
            base.title("Formulario Python")

            # Inicia el bucle principal de la aplicación tkinter para que la ventana se mantenga abierta
            base.mainloop()

        # Captura cualquier excepción ValueError que ocurra durante la ejecución del código en el bloque try
        except ValueError as error:
            # Imprime un mensaje de error si se produce una excepción ValueError
            print("Error al mostrar la interfaz,error: {}".format(error))


# Llama al método Formulario de la clase FormularioClientes para ejecutar la aplicación
FormularioClientes.Formulario()
