from guiCalculator import Calc
from logicCalculator import LogicCalculator

# Me tocó aprender un nuevo concepto, "Inyección de dependencia". Con esa madre hice que esta otra madre 
# se ejecute correctamente.

if __name__=="__main__":
    app = Calc()
    logic = LogicCalculator(app.entrada)
    app.crear_btns(logic.botones)



    
    app.on()

    