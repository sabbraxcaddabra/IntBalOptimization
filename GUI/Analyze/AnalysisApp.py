import matplotlib.pyplot as plt
import sys
import analysisGUI                           #конвертированный в .py фал дизайна окна анализа
from PyQt5.QtGui import QFont
from InternalBallistics.Analyze.SolveIntBal import solve_ib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from PyQt5 import QtWidgets, Qt, QtCore, QtGui

from PyQt5.QtWidgets import QMessageBox, QHeaderView



# В этом классе прописываются все взаимодействия с окно АНАЛИЗА
class AnalysisApp(QtWidgets.QMainWindow, analysisGUI.Ui_Dialog):   #Поменять название Ui_Dialog
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
        #self.short_res_textEdit.setReadOnly(True)
        self.butt_raschet.clicked.connect(self.do_raschet)
        self.plot_comboBox.view().pressed.connect(self.handleItemPressed)

    def first_row_text(self):
        if len(self.int_bal_cond.charge) == 1:
            pass
        else:
            a = Qt.QTableWidgetItem(u"\u03C8"+"₀")

            # Ставим жирный шрифт у заголовка
            fontBold = QFont()
            fontBold.setBold(True)
            a.setFont(fontBold)
            self.result_table.setHorizontalHeaderItem(3, a)

            for i in range(1, len(self.int_bal_cond.charge)):
                #Делаем красивые индексы
                powder_num = str(i)
                SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
                LowIndex = powder_num.translate(SUB)
                a = Qt.QTableWidgetItem(u"\u03C8"+LowIndex)
                # Ставим жирный шрифт у заголовков
                fontBold = QFont()
                fontBold.setBold(True)
                a.setFont(fontBold)

                self.result_table.insertColumn(3 + i)
                self.result_table.setHorizontalHeaderItem(3+i, a)                           # ВОТ ТУТ ВМЕСТЕ С ВАДИМОМ ГЛЯНУТЬ
                a = Qt.QTableWidgetItem('0.')
                self.result_table.setItem(0, 3+i, a)

        PV = str(self.int_bal_cond.PV * 1e-6)
        for k in range(3+len(self.int_bal_cond.charge), len(self.int_bal_cond.charge)+6):
            a = Qt.QTableWidgetItem(PV)
            self.result_table.setItem(0, k, a)



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

        ts, ys, p_mean, p_sn, p_kn = solve_ib(*self.int_bal_cond.create_params_tuple(), method=methods[method_], tstep=tau)

        self.lineEdit_GunSpeed.setText(str(round(ys[0][-1], 1)))
        self.lineEdit_AverPress.setText(str(round(max(p_mean)*1e-6, 2)))

        self.current_result = {
            'ts':ts,
            'ys':ys,
            'p_mean':p_mean,
            'p_sn':p_sn,
            'p_kn':p_kn
        }
        self._fill_result_table()
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
    def _fill_result_table(self):
        """
        Заполнение таблицы результатов
        :return:
        """
        for timestep in range(len(self.current_result['ts'])):
            self.result_table.insertRow(timestep+1)
            a = Qt.QTableWidgetItem(str(round(self.current_result['ts'][timestep]*1e3, 2)))
            self.result_table.setItem(timestep, 0, a)
            for index, y in enumerate(self.current_result['ys'], start=1):
                a = Qt.QTableWidgetItem(str(round(y[timestep], 2)))
                self.result_table.setItem(timestep, index, a)
            p_map = map(self.current_result.get, ('p_mean', 'p_sn', 'p_kn'))

            for i, p in enumerate(p_map, start=index+1):
                a = Qt.QTableWidgetItem(str(round(p[timestep]*1e-6, 2)))
                self.result_table.setItem(timestep, i, a)



def AnalWin():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("E3.ico"))
    InitWindow = AnalysisApp(int_bal_cond=int_bal_cond)
    InitWindow.show()
    sys.exit(app.exec_())

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
        Powder(name='6/7', omega=0.01, rho=1.6e3, f_powd=988e3, Ti=2800., Jk=343.8e3, alpha=1.038e-3, teta=0.236,
               Zk=1.53, kappa1=0.239, lambd1=2.26, mu1=0., kappa2=0.835, lambd2=-0.943, mu2=0.))
    int_bal_cond.add_powder(
        Powder(name='6/7', omega=0.01, rho=1.6e3, f_powd=988e3, Ti=2800., Jk=343.8e3, alpha=1.038e-3, teta=0.236,
               Zk=1.53, kappa1=0.239, lambd1=2.26, mu1=0., kappa2=0.835, lambd2=-0.943, mu2=0.))



if __name__ =='__main__':
    AnalWin()


