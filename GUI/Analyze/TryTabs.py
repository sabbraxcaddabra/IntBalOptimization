from PyQt5 import QtCore, QtGui, QtWidgets, Qt

import sys
from InternalBallistics.Analyze.SolveIntBal import solve_ib
from InternalBallistics.IntBalClasses import ArtSystem, Powder, IntBalParams

import TryToMakeTabs

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class AnalyzeApp(QtWidgets.QMainWindow, TryToMakeTabs.Ui_Dialog):
    def __init__(self, parent=None, int_bal_cond=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.int_bal_cond = int_bal_cond

        self.first_row_text()


        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.plot_Layout.addWidget(self.toolbar)
        self.plot_Layout.addWidget(self.canvas)

        self.current_result = None

        self.short_res_textEdit.setReadOnly(True)

        self.butt_raschet.clicked.connect(self.do_raschet)

        self.plot_comboBox.view().pressed.connect(self.handleItemPressed)


    def first_row_text(self):
        if len(self.int_bal_cond.charge) == 1:
            pass
        else:
            a = Qt.QTableWidgetItem(u"\u03C80")
            self.result_table.setHorizontalHeaderItem(3, a)
            for i in range(1, len(self.int_bal_cond.charge)):
                powder_num = str(i)
                #string = u'{string}'.format(string=string)
                a = Qt.QTableWidgetItem(u"\u03C8{powder_num}".format(powder_num=powder_num))
                self.result_table.insertColumn(3 + i)
                self.result_table.setHorizontalHeaderItem(3+i, a)
                a = Qt.QTableWidgetItem('0.')
                self.result_table.setItem(0, 3+i, a)

    def handleItemPressed(self, index):
        item = self.plot_comboBox.model().itemFromIndex(index)
        self.plot_(item.text())

    def do_raschet(self):

        methods = {
            'Метод Рунге-Кутты 4-го порядка':'RK4',
            'Метод Адамса-Башфорда 5-го порядка':'AB5'
        }

        method_ = self.method_comboBox.currentText()

        tau = float(self.step_lineEdit.text())

        ys, p_mean, p_sn, p_kn = solve_ib(*self.int_bal_cond.create_params_tuple(), method=methods[method_], tstep=tau)
        res = (
            f"Дульная скорость, м/с: {round(ys[0][-1], 1)}",
            f"Максимальное среднебаллистическое давление, MПа: {round(max(p_mean)*1e-6, 2)}"
        )
        res = '\n'.join(res)
        self.short_res_textEdit.setText(res)

        self.current_result = {
            'ys':ys,
            'p_mean':p_mean,
            'p_sn':p_sn,
            'p_kn':p_kn
        }

        self.plot_()

        self.plot_comboBox.setCurrentIndex(1)


    def plot_(self, grafics_dict_key='Среднебаллистическое давление'):
        plot_dict = {
            'Среднебаллистическое давление': (self._pressure_graphics, ('p_mean', 'Среднебаллистическое давление')),
            'Давление на дно снаряда': (self._pressure_graphics, ('p_sn', 'Давление на дно снаряда')),
            'Давление на дно канала ствола': (self._pressure_graphics, ('p_kn', 'Давление на дно канала ствола')),
            'Скорость': (self._velocity_graphic, ('Скорость снаряда',))

        }
        if grafics_dict_key == '-':
            pass
        try:
            plot_dict[grafics_dict_key][0](*plot_dict[grafics_dict_key][1])
        except:
            print("Нет данных для расечта")
    def _pressure_graphics(self, vals='p_mean', title='Среднебаллистическое давление'):
        pressure = self.current_result[vals] * 1e-6
        l_d = self.current_result['ys'][1]
        # instead of ax.hold(False)
        self.figure.clear()
        # create an axis
        ax = self.figure.add_subplot(111)
        # discards the old graph
        # ax.hold(False) # deprecated, see above
        # plot data
        ax.plot(l_d, pressure)
        # max_index = np.argmax(pressure)
        # ax.scatter(l_d[max_index], pressure[max_index])
        ax.set_title(title)
        ax.set_xlabel('Координата по стволу Ld, м')
        ax.set_ylabel('Давление P, МПа')
        ax.set_xlim(right=1.1 * l_d[-1])
        ax.set_ylim(top=1.1 * max(pressure))
        ax.grid()

        # refresh canvas
        self.canvas.draw()

    def _velocity_graphic(self, title='Скорость снаряда'):
        velocity = self.current_result['ys'][0]
        l_d = self.current_result['ys'][1]

        self.figure.clear()
        # create an axis
        ax = self.figure.add_subplot(111)
        # discards the old graph
        # ax.hold(False) # deprecated, see above
        # plot data
        ax.plot(l_d, velocity)

        ax.set_title(title)
        ax.set_xlim(right=1.1 * l_d[-1])
        ax.set_ylim(top=1.1 * max(velocity))
        ax.set_xlabel('Координата по стволу Ld, м')
        ax.set_ylabel('Скорость V, м/с')
        ax.grid()

        self.canvas.draw()


def StartApp():
    artsys = ArtSystem(name='2А42', d=.03, S=0.000735299, q=0.389, W0=0.125E-3, l_d=2.263, l_k=0.12,
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

    app = QtWidgets.QApplication(sys.argv)
    MyWindow = AnalyzeApp(int_bal_cond=int_bal_cond)
    MyWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    StartApp()