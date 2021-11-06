import sys
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets, Qt, QtCore, QtGui
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from InternalBallistics.Analyze.SolveIntBal import solve_ib
from InternalBallistics.IntBalClasses import ArtSystem, Powder, IntBalParams
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar



import artsysGUI                             #конвертированный в .py фал дизайна окна хар-к арт. ситсем
import initGUI                               #конвертированный в .py фал дизайна окна исходных данных
import powdersGUI                            #конвертированный в .py фал дизайна окна характеристик порохов
import analysisGUI                           #конвертированный в .py фал дизайна окна анализа

# В этом классе прописываются все взаимодействия с окном ИСХОДНЫХ ДАННЫХ
class InitApp(QtWidgets.QMainWindow, initGUI.Ui_initWindow):
    selCellDel = None  # Переменная хранит в себе выбранную строку для удаления(в таблице исходных данных порохов)
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #Обработка событий
        self.act_powders.triggered.connect(self.PowdersWin)                 # Вызываем окно базы порохов
        self.act_artsys.triggered.connect(self.ArtSysWin)                   # Вызываем окно базы арт.систем
        self.butt_add.clicked.connect(self.addColumnPowder)                 # Добавляет пустую колонку для пороха
        self.tableInitPowders.horizontalHeader().sectionClicked.connect(self.selDelColumnPowder)           # Отслеживаем клик по шапке строки
        self.butt_del.clicked.connect(self.delColumnPowder)                 # Удаляет последнюю колонку в таблице порохов
        self.act_save.triggered.connect(self.FileSave)                      # Вызывваем окно сохранения файла
        self.act_open.triggered.connect(self.FileOpen)                      # Вызываем окно открытия файла
        self.butt_anal.clicked.connect(self.StartAnalysis)                          # Вызываем окно анализа


    # Метод добавляет колонку для пороха
    def addColumnPowder(self):
        count = self.tableInitPowders.columnCount()         #Определяем текущее количество колонок
        self.tableInitPowders.insertColumn(count)           #Вставляем новую колонку
        #Вызываем свой метод чтобы отцентрировать текст в ячейках колонки
        self.CellAlignCenter(count)
    # Обрабатываем выбор колонки для удаления пороха
    def selDelColumnPowder(self):
        self.selCellDel = self.tableInitPowders.currentColumn()+1
        if self.selCellDel == 0:
            self.selCellDel = None

    # Метод удаляет колонку для пороха
    def delColumnPowder(self):
        if self.selCellDel is not None:
            delCol = QMessageBox()
            delCol.setWindowTitle("Подтверждение")
            delCol.setText("Вы точно хотите удалить колонку №"+str(self.selCellDel)+'?')
            delCol.setIcon(QMessageBox.Warning)
            delCol.setStandardButtons(QMessageBox.Cancel|QMessageBox.Yes)

            buttY = delCol.button(QMessageBox.Yes)
            buttY.setText("Да")

            buttCancel = delCol.button(QMessageBox.Cancel)
            buttCancel.setText("Отмена")

            res = delCol.exec()
            if res == QMessageBox.Yes:
                self.tableInitPowders.removeColumn(self.selCellDel-1)
                if (self.selCellDel-1) == 0:
                    self.selCellDel = None
        else:
            errordelCol = QMessageBox()
            errordelCol.setWindowTitle("Ошибка")
            errordelCol.setText("Колонка не выбрана!")
            errordelCol.setIcon(QMessageBox.Critical)
            errordelCol.setStandardButtons(QMessageBox.Cancel)
            buttCancel = errordelCol.button(QMessageBox.Cancel)
            buttCancel.setText("Отмена")
            errordelCol.exec()
    # Метод вызывает окно характеристик порохов
    def PowdersWin(self):
        self.DialogPowd = PowdersApp(self)
        self.DialogPowd.show()
    # Метод вызывает окно характеристик арт. систем
    def ArtSysWin(self):
        self.DialogArtSys = ArtSysApp(self)
        self.DialogArtSys.show()

    # Метод вызывает окно анализа
    def StartAnalysis(self):
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
        self.DialogAnalysis = AnalysisApp(int_bal_cond=int_bal_cond)
        self.DialogAnalysis.show()



    # Метод производит сохранение файла
    def FileSave(self):
        name = "InitSave.txt"
        direct = QDir.currentPath()
        filename = QFileDialog.getSaveFileName(self,"Сохранение исходных данных", direct+"/"+name, "TXT (*.txt)")[0]
        try:
            with open(filename, 'w', encoding='utf8') as f:
                # Считываем и сохраняем давление форсирования
                line = self.val_PressForc.text()
                f.write(line+'\n')
                # Считываем и сохраняем давление воспламенителя
                line = self.val_PressIgnit.text()
                f.write(line+'\n')

                # Считываем и сохраняем характеристики арт. системы
                for i in range(9):
                    val = self.tableInitArtSys.item(i, 0).text()
                    if i == 0:
                        val = val.replace(' ', '_')         #Возвращаем на место нижние подчёркивания в названии пороха, чтобы не было проблем с чтением файла
                    f.write(val+" ")
                f.write('\n')

                # Считываем и сохраняем характеристики порохов
                AllCol = self.tableInitPowders.columnCount()        #Узнаём текущее количество порохов
                for j in range(AllCol):
                    for i in range(15):
                        val = self.tableInitPowders.item(i, j).text()
                        if i == 0:
                            val = val.replace(' ','_')  # Возвращаем на место нижние подчёркивания в названии пороха, чтобы не было проблем с чтением файла
                        f.write(val + " ")
                    f.write('\n')
        except FileNotFoundError:
            pass


    # Метод производит открытия файла сохранения
    def FileOpen(self):
        name = "InitSave.txt"
        direct = QDir.currentPath()
        filename = QFileDialog.getOpenFileName(self,"Открыть исходные данные", direct+"/"+name, "TXT (*.txt)")[0]

        try:
            with open(filename, 'r', encoding='utf8') as f:
                #Считываем и сохраняем давление форсирования

                line = f.readline()
                self.val_PressForc.setText(line.strip())

                # Считываем и сохраняем давление воспламенителя
                line = f.readline()
                self.val_PressIgnit.setText(line.strip())

                # # Считываем и сохраняем характеристики арт. системы
                line = f.readline()
                line = line.split(' ')
                for i in range(9):
                    if i == 0:
                        line[i] = line[i].replace("_", " ")
                    a = Qt.QTableWidgetItem(str(line[i]))
                    a.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableInitArtSys.setItem(i, 0, a)

                # Считываем и сохраняем характеристики порохов
                count = 0
                for line in f:
                    self.tableInitPowders.insertColumn(count)
                    currline = line.split(' ')
                    for i in range(15):
                        if i == 0:
                            currline[i] = currline[i].replace("_"," ")
                        a = Qt.QTableWidgetItem(str(currline[i]))
                        a.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.tableInitPowders.setItem(i, count, a)
                    count += 1

        except FileNotFoundError:
            pass

    # Метод добавляет выбранный порох в таблицу
    def sel_Powder(self, CharPowder):
        #Считываем текущее количество колонок
        curColumns = self.tableInitPowders.columnCount()
        #Исключение если хотя бы одна колонка уже есть(если срабатывает то используем insert)
        if curColumns == 0:
            self.tableInitPowders.setColumnCount(1)
            #Вызываем свой метод чтобы отцентрировать текст в ячейках колонки
            self.CellAlignCenter(1)
        else:
            self.tableInitPowders.insertColumn(curColumns)
            #Вызываем свой метод чтобы отцентрировать текст в ячейках колонки
            self.CellAlignCenter(curColumns)

        #Тут вставляем название пороха
        a = Qt.QTableWidgetItem(CharPowder[0])
        a.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableInitPowders.setItem(0, curColumns, a)

        #А тут вставляем остальные характеристики
        for i in range(1, 14):
            a = Qt.QTableWidgetItem(CharPowder[i])
            a.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableInitPowders.setItem(i+1, curColumns, a)

    # Метод добавляет выбранную арт. систему в таблицу
    def sel_ArtSys(self, CharArtSys):
        #Вставляем название орудия
        a = Qt.QTableWidgetItem(CharArtSys[0])
        a.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableInitArtSys.setItem(0, 0, a)
        # Вставляем калибр орудия
        a = Qt.QTableWidgetItem(CharArtSys[1])
        a.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableInitArtSys.setItem(1, 0, a)
        #Вставляем всё остальное
        for i in range(2, 8):
            a = Qt.QTableWidgetItem(CharArtSys[i])
            a.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableInitArtSys.setItem(i+1, 0, a)



    #Метод настраивает центрирование текста в ячейках таблицы порохов(в новых колонках)
    def CellAlignCenter(self, Column):
        for i in range(14):
            item = QtWidgets.QTableWidgetItem()  # вот тут в одну функцию сделать
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableInitPowders.setItem(i, Column, item)


# В этом классе прописываются все взаимодействия с окном ХАРАКТЕРИСТИК ПОРОХОВ
class PowdersApp(QtWidgets.QMainWindow, powdersGUI.Ui_DialogPowders):
    selCellPowd = None # Переменная хранит в себе выбранную строку в базе порохов
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)                  #Инициилизация дизайна
#Считывание порохов из базы в таблицу
        header = self.tableCharPowders.horizontalHeader()
        F = open('PowdersBase.txt', 'r', encoding='utf8')                                               #Открываем файл
        row = 0                                                                                         #Объявляем счётчик для номера колонки
        for line in F:                                                                                  #Цикл бежит по строкам файла
            curLine = line.split()                                                                      #Строку файла приводим к кортежу, разделитель - пробел
            for col in range(14):                                                                       #Цикл бежит по колонкам
                if col == 0:                                                                            #Здесь просто убираем разделитель в
                    curLine[col] = curLine[col].replace("_"," ")                                        #названии пороха для красоты
                valcell = Qt.QTableWidgetItem(curLine[col])                                             #Говорим что в переменной айтем для таблицы
                valcell.setTextAlignment(QtCore.Qt.AlignCenter)                                         #Размещаем текст по центру ячейки
                header.setSectionResizeMode(col, QtWidgets.QHeaderView.ResizeToContents)                #Подгоняем ширину колонки под текст
                valcell.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)                  #Отключаем возможность редакт. ячейку
                self.tableCharPowders.setItem(row, col , valcell)                                       #Вставляем айтем в ячейку
            row += 1                                                                                    #Увеличиваем счётчик для перехода на новую строку
            self.tableCharPowders.insertRow(row)                                                        #Добавляем новую строку за текущей
        self.tableCharPowders.removeRow(row)                                                            #В конце удаляем лишнюю строку
        F.close()                                                                                       #Закрываем файл


        self.tableCharPowders.verticalHeader().sectionClicked.connect(self.selPowder)           # Отслеживаем клик по шапке строки
        self.butt_PowdersAdd.clicked.connect(self.AddPowder)                                    # Добавляем выбранный порох
        self.butt_PowdersClose.clicked.connect(self.close)                                      # Закрываем базу порохов по кнопке "Закрыть"


    #Обрабатываем выбор пороха и присваеваем номер выбранного пороха
    def selPowder(self):
        self.selCellPowd = self.tableCharPowders.currentRow()

    #Передаём выбранный порох в главное окно, если порох не выбран сделать диалоговое окно с ошибкой
    def AddPowder(self):
        charPowders = []
        if self.selCellPowd is not None:
            col = 0
            for i in range(14):
                val = self.tableCharPowders.item(self.selCellPowd, col).text()
                charPowders.append(val)
                col += 1
            self.parent.sel_Powder(charPowders)
            self.close()
        else:
            errorSelPowd = QMessageBox()
            errorSelPowd.setWindowTitle("Ошибка")
            errorSelPowd.setText("Выберите порох!")
            errorSelPowd.setIcon(QMessageBox.Critical)
            errorSelPowd.setStandardButtons(QMessageBox.Ok)
            errorSelPowd.exec()

# В этом классе прописываются все взаимодействия с окном ХАРАКТЕРИСТИК АРТ. СИСТЕМ
class ArtSysApp(QtWidgets.QMainWindow, artsysGUI.Ui_DialogArtSys):
    selCellArt = None # Переменная хранит в себе выбранную строку в базе арт. систем
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
    # Считывание арт систему из базы в таблицу
        header = self.tableCharArtSys.horizontalHeader()
        F = open('ArtSysBase.txt', 'r', encoding='utf8')
        row = 0
        for line in F:
            curLine = line.split()
            for col in range(8):
                if col == 0:
                    curLine[col] = curLine[col].replace("_", " ")
                valcell = Qt.QTableWidgetItem(curLine[col])
                valcell.setTextAlignment(QtCore.Qt.AlignCenter)
                header.setSectionResizeMode(col, QtWidgets.QHeaderView.ResizeToContents)
                valcell.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tableCharArtSys.setItem(row, col , valcell)
            row += 1
            self.tableCharArtSys.insertRow(row)
        self.tableCharArtSys.removeRow(row)
        F.close()

        #Обрабатываем события
        self.tableCharArtSys.verticalHeader().sectionClicked.connect(self.selArtSys)           # Отслеживаем клик по шапке строки
        self.butt_ArtSysClose.clicked.connect(self.close)                                           # Закрываем базу арт. систем по кнопке "Закрыть"
        self.butt_ArtSysAdd.clicked.connect(self.AddArtSys)                                       # Добавляем арт. систему из базы по кнопке "Добавить"


    #Обрабатываем выбор арт. системы и присваеваем номер выбранного пороха
    def selArtSys(self):
        self.selCellArt = self.tableCharArtSys.currentRow()

    #Передаём выбранную арт. систему в главное окно, если система не выбрана сделать диалоговое окно с ошибкой
    def AddArtSys(self):
        charArtSys = []
        if self.selCellArt is not None:
            col = 0
            for i in range(8):
                val = self.tableCharArtSys.item(self.selCellArt, col).text()
                charArtSys.append(val)
                col += 1
            self.parent.sel_ArtSys(charArtSys)
            self.close()
        else:
            errorSelArtSys = QMessageBox()
            errorSelArtSys.setWindowTitle("Ошибка")
            errorSelArtSys.setText("Выберите арт. систему!")
            errorSelArtSys.setIcon(QMessageBox.Critical)
            errorSelArtSys.setStandardButtons(QMessageBox.Ok)
            errorSelArtSys.exec()

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








#Функция вызывает окно исходных данных
def InitWin():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("E3.ico"))
    InitWindow = InitApp()
    InitWindow.show()
    sys.exit(app.exec_())

#Условие для запуска
if __name__ =='__main__':
    InitWin()


