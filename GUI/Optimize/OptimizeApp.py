import numpy as np

from GUI.Optimize import optimizGUI                      #конвертированный в .py фал дизайна окна анализа
from PyQt5 import QtWidgets, Qt, QtCore, QtGui
from PyQt5.QtCore import QThread
import time

from InternalBallistics.Optimize.SolveIntBal import solve_ib
from InternalBallistics.Optimize.IntBalOptimizer import IntBalOptimizer
from InternalBallistics.ErrorClasses import *
from InternalBallistics.ErrorClasses import *


class MyThread(QThread):

    def __init__(self, parent):
        QThread.__init__(self)
        self.parent = parent


    def run(self):

        methods = {
            'Случайный поиск': 'random_search',
            'Случайное сканирование': 'random_scan'
        }

        method = methods[self.parent.comboBox_MethOptimize.currentText()]

        self.int_bal_cond = self.parent.parent.set_int_bal_cond()

        x_vec = []

        for powd in self.int_bal_cond.charge:
            x_vec.extend((powd.omega, powd.Jk))

        x_vec = np.array(x_vec)



        combo_index = self.parent.comboBox_MethOptimize.currentIndex()

        if combo_index == 0:
            x_lims = [[0, np.inf] for _ in range(len(x_vec))]
        else:
            powd_mass_lim = float(self.val_massPowd.text())/100.

            finit_imp_lim = float(self.val_FinitImpuls.text())/100

            x_lims = [[0., powd.omega + powd_mass_lim*powd.omega] for powd in self.int_bal_cond.charge] + \
                [[powd.Jk - finit_imp_lim*powd.Jk, powd.Jk + finit_imp_lim*powd.Jk] for powd in self.int_bal_cond.charge]

        max_delta = float(self.parent.val_maxDensity.text())

        p_max = float(self.parent.val_maxPress.text()) * 1e6
        max_eta_k = float(self.parent.val__coordGor.text())



        optimizer = IntBalOptimizer(x_vec, params=self.int_bal_cond, out_func=self.out_func, Pmax=p_max, max_eta_k=max_eta_k, delta_max=max_delta, x_lims=x_lims)
        optimized_xvec = optimizer.optimize_with_Jk(method)

        # if self.parent.checkBox_SelComp.isChecked():
        #     self.pick_up_optimum_charge(optimizer, optimized_xvec)

    def out_func(self, x_vec, f, sol, params):
        text = f"Масса снаряда: {params.syst.q = } кг\n"
        for powd in params.charge:
            text += f"Масса пороха {powd.name}: {round(powd.omega, 4)} кг\n"
            text += f"Конечный импульс пороха {powd.name}: {round(powd.Jk, 2)} Па*с\n"
        text += f"Дульная скорость: {-round(f, 1)} м/с\n"
        text += f"Максимальное среднебаллистическое давление: {round(sol[0] * 1e-6, 2)} МПа\n"
        text += f"Максимальное давление на дно снаряда: {round(sol[1] * 1e-6, 2)} МПа\n"
        text += f"Максимальное давление на дно канала ствола: {round(sol[2] * 1e-6, 2)} МПа\n"
        text += f"Координата полного сгорания порохового заряда {round(sol[3], 4)} м\n"
        text += "*" * 30 + '\n'

        self.parent.textBrowser_optimize.append(text)

        time.sleep(0.1)

def out_bal_func1(x_vec, f, sol, params):
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
class OptimizeApp(QtWidgets.QMainWindow, optimizGUI.Ui_OptimizeWindow):   #Поменять название Ui_Dialog
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.butt_Start.clicked.connect(self.do_optimize)

        self.comboBox_MethOptimize.view().pressed.connect(self.handleItemPressed)

    def handleItemPressed(self, index):
        item = self.comboBox_MethOptimize.model().itemFromIndex(index)
        if item.row() == 1:
            self.label_massPowd.setEnabled(True)
            self.label_FinitImpuls.setEnabled(True)
            self.val_massPowd.setEnabled(True)
            self.val_FinitImpuls.setEnabled(True)
        if item.row() == 0:
            self.label_massPowd.setDisabled(True)
            self.label_FinitImpuls.setDisabled(True)
            self.val_massPowd.setDisabled(True)
            self.val_FinitImpuls.setDisabled(True)

        #item = self.plot_comboBox.model().itemFromIndex(index)



    def do_optimize(self):

        self.thread = MyThread(self)
        self.thread.start()



        # methods = {
        #     'Случайный поиск': 'random_search',
        #     'Случайное сканирование': 'random_scan'
        # }
        #
        # method = methods[self.comboBox_MethOptimize.currentText()]
        #
        # self.int_bal_cond = self.parent.set_int_bal_cond()
        #
        # x_vec = []
        #
        # for powd in self.int_bal_cond.charge:
        #     x_vec.extend((powd.omega, powd.Jk))
        #
        # x_vec = np.array(x_vec)
        #
        #
        #
        # combo_index = self.comboBox_MethOptimize.currentIndex()
        #
        # if combo_index == 0:
        #     x_lims = [[0, np.inf] for _ in range(len(x_vec))]
        # else:
        #     powd_mass_lim = float(self.val_massPowd.text())/100.
        #
        #     finit_imp_lim = float(self.val_FinitImpuls.text())/100
        #
        #     x_lims = [[0., powd.omega + powd_mass_lim*powd.omega] for powd in self.int_bal_cond.charge] + \
        #         [[powd.Jk - finit_imp_lim*powd.Jk, powd.Jk + finit_imp_lim*powd.Jk] for powd in self.int_bal_cond.charge]
        #
        # max_delta = float(self.val_maxDensity.text())
        #
        # p_max = float(self.val_maxPress.text()) * 1e6
        # max_eta_k = float(self.val__coordGor.text())
        #
        #
        #
        # optimizer = IntBalOptimizer(x_vec, params=self.int_bal_cond, out_func=self.out_func, Pmax=p_max, max_eta_k=max_eta_k, delta_max=max_delta, x_lims=x_lims)
        # optimized_xvec = optimizer.optimize_with_Jk(method)
        #
        # if self.checkBox_SelComp.isChecked():
        #     self.pick_up_optimum_charge(optimizer, optimized_xvec)


    def pick_up_optimum_charge(self, optimizer, optimized_xvec, method='random_search'):

        self.textBrowser_optimize.clear()
        optimizer.out_func = None
        optimizer.set_combo_out_func(self.combo_out_func)

        optimized_combos = optimizer.get_optimized_powders_mass(optimized_xvec, method)

    def out_func(self, x_vec, f, sol, params):
        text = f"Масса снаряда: {params.syst.q = } кг\n"
        for powd in params.charge:
            text += f"Масса пороха {powd.name}: {round(powd.omega, 4)} кг\n"
            text += f"Конечный импульс пороха {powd.name}: {round(powd.Jk, 2)} Па*с\n"
        text += f"Дульная скорость: {-round(f, 1)} м/с\n"
        text += f"Максимальное среднебаллистическое давление: {round(sol[0] * 1e-6, 2)} МПа\n"
        text += f"Максимальное давление на дно снаряда: {round(sol[1] * 1e-6, 2)} МПа\n"
        text += f"Максимальное давление на дно канала ствола: {round(sol[2] * 1e-6, 2)} МПа\n"
        text += f"Координата полного сгорания порохового заряда {round(sol[3], 4)} м\n"
        text += "*" * 30 + '\n'

        self.textBrowser_optimize.append(text)

    def combo_out_func(self, combo):

        self.textBrowser_optimize.append(str(combo))
