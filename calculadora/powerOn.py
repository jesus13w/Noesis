from guiCalculator import Calc
from logicCalculator import LogicCalculator


if __name__=="__main__":
    app = Calc()
    logic = LogicCalculator()
    app.crear_btns(logic.botones)


    
    app.on()