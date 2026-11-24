from gestorNotasInterfaz import NoteManager
from gestorNotasLogica import LogicNoteManagement




if __name__ == "__main__":
    app = NoteManager()
    app.g_widgets()

    app.createTableGradeManagement()

    logic = LogicNoteManagement(app.tableOfGrade)
    print(logic.__dict__)

    app.createButton(logic.buttonActionGradeManagement)
    

    app.powerOn()