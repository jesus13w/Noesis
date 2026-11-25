import tkinter as tk
class LogicCalculator:

    def __init__(self, entrada):
        self.entrada = entrada
        
        
        self.botones=[

            ("1", lambda : self.escribir("1")),
            ("2", lambda : self.escribir("2")),
            ("3", lambda : self.escribir("3")),
            ("c", self.borrar),
            ("4", lambda : self.escribir("4")),
            ("5", lambda : self.escribir("5")),
            ("6", lambda : self.escribir("6")),
            ("+", lambda : self.escribir("+")),
            ("7", lambda : self.escribir("7")),
            ("8", lambda : self.escribir("8")),
            ("9", lambda : self.escribir("9")),
            ("-", lambda : self.escribir("-")),
            ("0", lambda : self.escribir("0")),
            ("/", lambda : self.escribir("/")),
            ("*", lambda : self.escribir("*")),
            ("=", self.calcular)
        ]

    # El problema era que mis funciones utilizan un widget/objeto llamado "self.entrada" y
    # la clase "LogicCalculator" no tiene ni puta idea de que es eso. Investigué por ahi
    # y encontre un nuevo término/concepto INYECCIÓN DE DEPENDENCIA, y con esa vaina resolví el problema.

    # Ignoren el hecho de que me estaba pegando una calculadora.


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

    

