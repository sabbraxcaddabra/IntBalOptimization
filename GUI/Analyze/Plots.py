from PyQt5 import QtWidgets
import sys

import PlotsGUI

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

"""
Окно графиков для mainGUI.py
"""
class PlotApp(QtWidgets.QMainWindow, PlotsGUI.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.verticalLayout.addWidget(self.toolbar)
        self.verticalLayout.addWidget(self.canvas)

        self.comboBox.view().pressed.connect(self.handleItemPressed)
        #self.plot_()

    def handleItemPressed(self, index):
        item = self.comboBox.model().itemFromIndex(index)
        self.plot_(item.text())

    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = [random.random() for i in range(10)]

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        # ax.hold(False) # deprecated, see above

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()

    def plot_(self, grafics_dict_key='Среднебаллистическое давление'):
        plot_dict = {
            'Среднебаллистическое давление': (self._pressure_graphics, ('p_mean', 'Среднебаллистическое давление')),
            'Давление на дно снаряда': (self._pressure_graphics, ('p_sn', 'Давление на дно снаряда')),
            'Давление на дно канала ствола': (self._pressure_graphics, ('p_kn', 'Давление на дно канала ствола')),
            'Скорость': (self._velocity_graphic, ('Скорость снаряда',))

        }
        plot_dict[grafics_dict_key][0](*plot_dict[grafics_dict_key][1])

    def _pressure_graphics(self, vals='p_mean', title='Среднебаллистическое давление'):
        pressure = self.parent.curent_result[vals] * 1e-6
        l_d = self.parent.curent_result['ys'][1]
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
        velocity = self.parent.curent_result['ys'][0]
        l_d = self.parent.curent_result['ys'][1]

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
    app = QtWidgets.QApplication(sys.argv)
    MyWindow = PlotApp()
    MyWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    StartApp()
