import sys
from InternalBallistics.Analyze.SolveIntBal import solve_ib
from InternalBallistics.IntBalClasses import ArtSystem, Powder, IntBalParams
from PyQt5 import QtWidgets
from Plots import PlotApp

import AnalyzeGUI

"""
Окно анализа с всплывающим окном графика
"""

class Res(QtWidgets.QMainWindow, AnalyzeGUI.Ui_Dialog):
    def __init__(self, parent=None) -> object:
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.curent_result = None
        self.butt_raschet.clicked.connect(self.do_raschet)
        self.graphics_button.clicked.connect(self.make_graphiks)

    def do_raschet(self):

        methods = {
            'Метод Рунге-Кутты 4-го порядка':'RK4',
            'Метод Адамса-Башфорда 5-го порядка':'AB5'
        }

        method_ = self.method_comboBox.currentText()

        tau = float(self.step_lineEdit.text())
        artsys = ArtSystem(name='2А42',  d=.03, S=0.000735299, q=0.389, W0=0.125E-3, l_d=2.263, l_k=0.12,
                           l0=0.125E-3 / 0.000735299, Kf=1.136)

        int_bal_cond = IntBalParams(syst=artsys, P0=50e6, PV=4e6)
        int_bal_cond.add_powder(
            Powder(name='6/7', omega=0.07, rho=1.6e3, f_powd=988e3, Ti=2800., Jk=343.8e3, alpha=1.038e-3, teta=0.236,
                   Zk=1.53, kappa1=0.239, lambd1=2.26, mu1=0., kappa2=0.835, lambd2=-0.943, mu2=0.))
        int_bal_cond.add_powder(
            Powder(name='6/7', omega=0.03, rho=1.6e3, f_powd=988e3, Ti=2800., Jk=343.8e3, alpha=1.038e-3, teta=0.236,
                   Zk=1.53, kappa1=0.239, lambd1=2.26, mu1=0., kappa2=0.835, lambd2=-0.943, mu2=0.))
        int_bal_cond.add_powder(
            Powder(name='6/7', omega=0.02, rho=1.6e3, f_powd=988e3, Ti=2800., Jk=343.8e3, alpha=1.038e-3, teta=0.236,
                   Zk=1.53, kappa1=0.239, lambd1=2.26, mu1=0., kappa2=0.835, lambd2=-0.943, mu2=0.))


        ys, p_mean, p_sn, p_kn = solve_ib(*int_bal_cond.create_params_tuple(), method=methods[method_], tstep=tau)
        res = (
            f"Дульная скорость, м/с: {round(ys[0][-1], 1)}",
            f"Максимальное среднебаллистическое давление, MПа: {round(max(p_mean)*1e-6, 2)}"
        )
        res = '\n'.join(res)
        self.short_res_textEdit.setText(res)

        self.curent_result = {
            'ys':ys,
            'p_mean':p_mean,
            'p_sn':p_sn,
            'p_kn':p_kn
        }

    def make_graphiks(self):
        if not self.curent_result:
            print("Нет данных для расчета!")
        else:
            self.plots = PlotApp(self)
            self.plots.show()
        # grafics_dict = {
        #     'Среднебаллистическое давление':[self._pressure_grafics, ('p_mean', 'Среднебаллистическое давление')],
        #     'Давление на дно снаряда':[self._pressure_graphics, ('p_sn', 'Давление на дно снаряда')],
        #     'Давление на дно канала ствола':self._pressure_graphics('p_kn', 'Давление на дно канала ствола'),
        #     'Скорость':[self._velocity_graphic, ('ys', 'Скорость снаряда',)]
        # }
        # if not self.curent_result:
        #     print("Нет данных для расчета")
        # else:
        #     pass

    # def _pressure_graphics(self, vals='p_mean', title='Среднебаллистическое давление'):
    #     pass
    #     #fig, ax = plt.subplots()
    # def _velocity_graphic(self, vals='ys', title='Скорость снаряда'):
    #     pass

def StartApp():
    app = QtWidgets.QApplication(sys.argv)
    MyWindow = Res()
    MyWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    StartApp()