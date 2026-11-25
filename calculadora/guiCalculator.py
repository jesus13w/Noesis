
import tkinter as tk
from tkinter import ttk

class Calc:
    def __init__(self):

        self.root=tk.Tk()
        self.root.geometry("250x310+500+100")
        self.root.resizable(False, False)
        

        self.entrada = ttk.Entry(self.root, font=("Arial", 12), justify="left")
        self.entrada.place(x=10, y=10, width=230, height=50)

        self.frame_btn = ttk.Frame(self.root)
        self.frame_btn.place(x=10, y=70, width=230, height=230)

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

    def crear_btns(self, botones):
        fila = 0
        columna=0

        for boton, accion in botones:
            btn = ttk.Button(self.frame_btn, text=boton, command=accion)
            btn.grid(row=fila, column=columna, pady=2, padx=2, sticky="nsew")
            btn.winfo_rgb(color="Black")

            columna+=1
            if columna == 4:
                columna=0
                fila +=1

        for i in range(4):
            self.frame_btn.columnconfigure(i, weight=1)
        for i in range(4):
            self.frame_btn.rowconfigure(i, weight=1)

    def on(self):
        self.root.mainloop()

if __name__=="__main__":
    app = Calc()

    botones=[

        ("1", lambda: app.escribir("1")),
        ("2", lambda: app.escribir("2")),
        ("3", lambda: app.escribir("3")),
        ("c", app.borrar),
        ("4", lambda: app.escribir("4")),
        ("5", lambda: app.escribir("5")),
        ("6", lambda: app.escribir("6")),
        ("+", lambda: app.escribir("+")),
        ("7", lambda: app.escribir("7")),
        ("8", lambda: app.escribir("8")),
        ("9", lambda: app.escribir("9")),
        ("-", lambda: app.escribir("-")),
        ("0", lambda: app.escribir("0")),
        ("/", lambda: app.escribir("/")),
        ("*", lambda: app.escribir("*")),
        ("=", app.calcular)
    ]

    app.crear_btns(botones)
    app.on()