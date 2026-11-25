
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

