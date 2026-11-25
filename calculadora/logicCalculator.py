import tkinter as tk
#from tkinter import ttk
class LogicCalculator:

    def __init__(self):
        
        self.botones=[

            ("1", self.escribir), #("1")),
            ("2", self.escribir), #("2")),
            ("3", self.escribir), #("3")),
            ("c", self.borrar),
            ("4", self.escribir), #("4")),
            ("5", self.escribir), #("5")),
            ("6", self.escribir), #("6")),
            ("+", self.escribir), #("+")),
            ("7", self.escribir), #("7")),
            ("8", self.escribir), #("8")),
            ("9", self.escribir), #("9")),
            ("-", self.escribir), #("-")),
            ("0", self.escribir), #("0")),
            ("/", self.escribir), #("/")),
            ("*", self.escribir), #("*")),
            ("=", self.calcular)
        ]

    


    def borrar(self):
        self.entrada.delete(0, tk.END)

    def escribir(self, texto):
        self.entrada.insert(tk.END, texto)


    def calcular(self):
        try:
            resultado = eval(self.entrada.get())
            self.borrar()
            self.entrada.insert(0, str(resultado))
        except:
            self.borrar()
            self.entrada.insert(0, "Error")

    

