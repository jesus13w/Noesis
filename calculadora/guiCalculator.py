import tkinter as tk
from tkinter import ttk

class InterfazCalculadora:
    def __init__(self):
        self.ventanaPrincipal = tk.Tk()
        self.ventanaPrincipal.title("Calculadora")
        self.ventanaPrincipal.geometry("250x300")
        self.ventanaPrincipal.resizable(False, False)

    def powerOn(self):
        self.ventanaPrincipal.mainloop()

if __name__ == "__main__":
    app = InterfazCalculadora()

    app.powerOn()
