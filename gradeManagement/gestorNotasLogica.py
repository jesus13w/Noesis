

class LogicNoteManagement:
    def __init__(self, tabla):

        self.tableOfGrade = tabla

        self.buttonActionGradeManagement = [

            ("➕ Add Grade", self.addNote),
            ("✏️ Edit Grade", self.editNote),
            ("⛔ Remove Gade", self.removeNote),
            ("🆗 Save", self.saveNote)
]
        

    def addNote(self):

        self.tableOfGrade.insert("", "end", values=("Bases de datos", 4.3, 10, "24/09/26", "Practíca"))

    def editNote(self):
        pass

    def removeNote(self):
        pass

    def saveNote(self):
        pass



