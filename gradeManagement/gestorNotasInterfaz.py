
import tkinter as tk
from tkinter import ttk

class NoteManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestor de notas")
        self.root.geometry("1300x800")
        self.root.resizable(False, False)
        self.root.configure(background="black")
        

    def g_widgets(self):
        #Widgets del lado izquierdo de la pantalla, datos del estudiante
        self.p_frame = ttk.LabelFrame(self.root, text="Detalles del estudiante")
        self.p_frame.place(relwidth=0.35, height=300, y=10, x=10)

        self.nameStudent = ttk.Label(self.p_frame, text="Nombre:", font=("Arial", 12))
        self.nameStudent.place(relx=1.0, x=-370, anchor="ne", y=20)
        self.eNameStudent = ttk.Entry(self.p_frame, font=("Aral", 12, "bold"), justify="left")
        self.eNameStudent.place(relwidth=0.75, height=30, relx=0.2, y=20)
        

        self.idStudent = ttk.Label(self.p_frame, text="ID:", font=("Arial", 12))
        self.idStudent.place(relx=1.0, x=-370, anchor="ne", y=60)
        self.eIdStudent = ttk.Entry(self.p_frame, font=("Aral", 12, "bold"), justify="left")
        self.eIdStudent.place(relwidth=0.75, height=30, relx=0.2, y=60)

        self.courseStudent = ttk.Label(self.p_frame, text="Curso:", font=("Arial", 12))
        self.courseStudent.place(relx=1.0, x=-370, anchor="ne", y=100)
        self.eCourseStudent = ttk.Entry(self.p_frame, font=("Aral", 12, "bold"), justify="left")
        self.eCourseStudent.place(relwidth=0.75, height=30, relx=0.2, y=100)

        self.semesterStudent = ttk.Label(self.p_frame, text="Semestre:", font=("Arial", 12))
        self.semesterStudent.place(relx=1.0, x=-370, anchor="ne", y=140)
        self.eSemesterStudent = ttk.Entry(self.p_frame, font=("Aral", 12, "bold"), justify="left")
        self.eSemesterStudent.place(relwidth=0.75, height=30, relx=0.2, y=140)


        self.viewCourses = ttk.LabelFrame(self.root, text="Cursos inscritos")
        self.viewCourses.place(relwidth=0.35, height=470, y=320, x=10)

        self.mViewCourses = tk.Text(self.viewCourses)
        self.mViewCourses.configure(state="disabled")
        self.mViewCourses.place(relwidth=0.9, height=430, relx=0.05)

        #Widgets del lado izquierdo

        self.grademanager = ttk.LabelFrame(self.root, text="Gestión de notas")
        self.grademanager.place(relwidth=0.625, relheight=.91, y=10, x=-10, relx=1.0, anchor="ne")

        self.viewAverage = ttk.Label(self.root)
        self.viewAverage.place(relwidth=0.625, relheight=.05, rely=1.0, y=-50, x=-10, relx=1.0, anchor="ne")

    def powerOn(self):
        self.root.mainloop()

        

    



    





    