
from GUI.Optimize import optimizGUI                      #конвертированный в .py фал дизайна окна анализа
from PyQt5 import QtWidgets, Qt, QtCore, QtGui

from InternalBallistics.Optimize.SolveIntBal import solve_ib
from InternalBallistics.ErrorClasses import *
from InternalBallistics.ErrorClasses import *


def out_bal_func(x_vec, f, sol, params):
    print(f"Масса снаряда: {params.syst.q = } кг")
    for powd in params.charge:
        print(f"Масса пороха {powd.name}: {round(powd.omega, 4)} кг")
        print(f"Конечный импульс пороха {powd.name}: {round(powd.Jk, 2)} Па*с")
    print(f"Дульная скорость: {-round(f, 1)} м/с")
    print(f"Максимальное среднебаллистическое давление: {round(sol[0] * 1e-6, 2)} МПа")
    print(f"Максимальное давление на дно снаряда: {round(sol[1] * 1e-6, 2)} МПа")
    print(f"Максимальное давление на дно канала ствола: {round(sol[2] * 1e-6, 2)} МПа")
    print(f"Координата полного сгорания порохового заряда {round(sol[3], 4)} м")
    print("*" * 30 + '\n')

# В этом классе прописываются все взаимодействия с окном ОПТИМИЗАЦИИ
class OptimizeApp(QtWidgets.QMainWindow, optimizGUI.Ui_MainOptimize):   #Поменять название Ui_Dialog
    def __init__(self, parent=None, int_bal_cond=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.int_bal_cond = int_bal_cond

        self.butt_Start.clicked.connect(self.do_optimize)


    def do_optimize(self):
        y, p_mean_max, p_sn_max, p_kn_max, lk = solve_ib(*self.int_bal_cond.create_params_tuple())

        print("Печать результатов рачета\n")
        print(f"Дульная скорость: {round(y[0], 1)} м/с")
        print(f"Максимальное среднебаллистическое давление: {round(p_mean_max * 1e-6, 2)} МПа")
        print(f"Максимальное давление на дно снаряда: {round(p_sn_max * 1e-6, 2)} МПа")
        print(f"Максимальное давление на дно канала ствола: {round(p_kn_max * 1e-6, 2)} МПа")
        print(f"Координата полного сгорания порохового заряда {round(lk, 4)} м")