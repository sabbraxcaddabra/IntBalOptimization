
from GUI.Optimize import optimizGUI                      #конвертированный в .py фал дизайна окна анализа

from PyQt5 import QtWidgets, Qt, QtCore, QtGui


# В этом классе прописываются все взаимодействия с окном ОПТИМИЗАЦИИ
class OptimizeApp(QtWidgets.QMainWindow, optimizGUI.Ui_MainOptimize):   #Поменять название Ui_Dialog
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
