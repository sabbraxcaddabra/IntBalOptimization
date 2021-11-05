import sys
from PyQt5 import QtWidgets, Qt, QtCore
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMessageBox, QFileDialog

import artsysGUI                             #конвертированный в .py фал дизайна окна хар-к арт. ситсем
import initGUI                               #конвертированный в .py фал дизайна окна исходных данных
import powdersGUI                            #конвертированный в .py фал дизайна окна характеристик порохов


#В этом классе прописываются все взаимодействия с окном ИСХОДНЫХ ДАННЫХ
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




#В этом классе прописываются все взаимодействия с окном ХАРАКТЕРИСТИК ПОРОХОВ
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



#В этом классе прописываются все взаимодействия с окном ХАРАКТЕРИСТИК АРТ. СИСТЕМ
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










#Функция вызывает окно исходных данных
def InitWin():
    app = QtWidgets.QApplication(sys.argv)
    InitWindow = InitApp()
    InitWindow.show()
    sys.exit(app.exec_())

#Условие для запуска
if __name__ =='__main__':
    InitWin()


