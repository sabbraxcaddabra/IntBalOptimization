# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\denis\PycharmProjects\BallOptimiz\init.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_initWindow(object):
    def setupUi(self, initWindow):
        initWindow.setObjectName("initWindow")
        initWindow.setEnabled(True)
        initWindow.resize(785, 630)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(initWindow.sizePolicy().hasHeightForWidth())
        initWindow.setSizePolicy(sizePolicy)
        initWindow.setMinimumSize(QtCore.QSize(785, 630))
        initWindow.setMaximumSize(QtCore.QSize(785, 630))
        font = QtGui.QFont()
        font.setPointSize(8)
        initWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(initWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.butt_anal = QtWidgets.QPushButton(self.centralwidget)
        self.butt_anal.setGeometry(QtCore.QRect(500, 560, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.butt_anal.setFont(font)
        self.butt_anal.setObjectName("butt_anal")
        self.butt_synth = QtWidgets.QPushButton(self.centralwidget)
        self.butt_synth.setGeometry(QtCore.QRect(640, 560, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.butt_synth.setFont(font)
        self.butt_synth.setObjectName("butt_synth")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 371, 581))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableInitPowders = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableInitPowders.setGeometry(QtCore.QRect(10, 30, 345, 491))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tableInitPowders.setFont(font)
        self.tableInitPowders.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableInitPowders.setAutoScrollMargin(10)
        self.tableInitPowders.setAlternatingRowColors(False)
        self.tableInitPowders.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableInitPowders.setObjectName("tableInitPowders")
        self.tableInitPowders.setColumnCount(0)
        self.tableInitPowders.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(14, item)
        self.butt_del = QtWidgets.QPushButton(self.groupBox_2)
        self.butt_del.setGeometry(QtCore.QRect(130, 530, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.butt_del.setFont(font)
        self.butt_del.setObjectName("butt_del")
        self.butt_add = QtWidgets.QPushButton(self.groupBox_2)
        self.butt_add.setGeometry(QtCore.QRect(230, 530, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.butt_add.setFont(font)
        self.butt_add.setObjectName("butt_add")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 10, 381, 331))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.tableInitArtSys = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableInitArtSys.setGeometry(QtCore.QRect(20, 40, 341, 272))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tableInitArtSys.setFont(font)
        self.tableInitArtSys.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableInitArtSys.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableInitArtSys.setAutoScrollMargin(10)
        self.tableInitArtSys.setObjectName("tableInitArtSys")
        self.tableInitArtSys.setColumnCount(1)
        self.tableInitArtSys.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitArtSys.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitArtSys.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitArtSys.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitArtSys.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitArtSys.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitArtSys.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitArtSys.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitArtSys.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitArtSys.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableInitArtSys.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableInitArtSys.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableInitArtSys.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableInitArtSys.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableInitArtSys.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableInitArtSys.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableInitArtSys.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableInitArtSys.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableInitArtSys.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableInitArtSys.setItem(8, 0, item)
        self.tableInitArtSys.horizontalHeader().setVisible(False)
        self.tableInitArtSys.verticalHeader().setVisible(True)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(390, 350, 381, 131))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 30, 341, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.val_PressForc = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.val_PressForc.setFont(font)
        self.val_PressForc.setText("")
        self.val_PressForc.setMaxLength(11)
        self.val_PressForc.setAlignment(QtCore.Qt.AlignCenter)
        self.val_PressForc.setObjectName("val_PressForc")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.val_PressForc)
        self.label_PressIgnit = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_PressIgnit.setFont(font)
        self.label_PressIgnit.setObjectName("label_PressIgnit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_PressIgnit)
        self.val_PressIgnit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.val_PressIgnit.setFont(font)
        self.val_PressIgnit.setMaxLength(11)
        self.val_PressIgnit.setAlignment(QtCore.Qt.AlignCenter)
        self.val_PressIgnit.setObjectName("val_PressIgnit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.val_PressIgnit)
        self.label_PressForc = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_PressForc.setFont(font)
        self.label_PressForc.setObjectName("label_PressForc")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_PressForc)
        initWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(initWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 785, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.menubar.setFont(font)
        self.menubar.setTabletTracking(False)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setObjectName("menubar")
        self.bases = QtWidgets.QMenu(self.menubar)
        self.bases.setObjectName("bases")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        initWindow.setMenuBar(self.menubar)
        self.act_powders = QtWidgets.QAction(initWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.act_powders.setFont(font)
        self.act_powders.setObjectName("act_powders")
        self.act_artsys = QtWidgets.QAction(initWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.act_artsys.setFont(font)
        self.act_artsys.setObjectName("act_artsys")
        self.act_open = QtWidgets.QAction(initWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.act_open.setFont(font)
        self.act_open.setObjectName("act_open")
        self.act_save = QtWidgets.QAction(initWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.act_save.setFont(font)
        self.act_save.setObjectName("act_save")
        self.action = QtWidgets.QAction(initWindow)
        self.action.setObjectName("action")
        self.bases.addAction(self.act_powders)
        self.bases.addAction(self.act_artsys)
        self.file.addAction(self.act_open)
        self.file.addAction(self.act_save)
        self.menu.addAction(self.action)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.bases.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(initWindow)
        QtCore.QMetaObject.connectSlotsByName(initWindow)

    def retranslateUi(self, initWindow):
        _translate = QtCore.QCoreApplication.translate
        initWindow.setWindowTitle(_translate("initWindow", "Программа кафедры Е3 - BallOptimize"))
        self.butt_anal.setText(_translate("initWindow", "Анализ"))
        self.butt_synth.setText(_translate("initWindow", "Синтез"))
        self.groupBox_2.setTitle(_translate("initWindow", "Характеристики метательного заряда:"))
        item = self.tableInitPowders.verticalHeaderItem(0)
        item.setText(_translate("initWindow", "Марка пороха: "))
        item = self.tableInitPowders.verticalHeaderItem(1)
        item.setText(_translate("initWindow", "Масса навески, кг: "))
        item = self.tableInitPowders.verticalHeaderItem(2)
        item.setText(_translate("initWindow", "Delta, кг/м³: "))
        item = self.tableInitPowders.verticalHeaderItem(3)
        item.setText(_translate("initWindow", "f, Дж/кг: "))
        item = self.tableInitPowders.verticalHeaderItem(4)
        item.setText(_translate("initWindow", "T1, К: "))
        item = self.tableInitPowders.verticalHeaderItem(5)
        item.setText(_translate("initWindow", "Iк, Па⋅с: "))
        item = self.tableInitPowders.verticalHeaderItem(6)
        item.setText(_translate("initWindow", "α, м³/кг: "))
        item = self.tableInitPowders.verticalHeaderItem(7)
        item.setText(_translate("initWindow", "θ: "))
        item = self.tableInitPowders.verticalHeaderItem(8)
        item.setText(_translate("initWindow", "Zк: "))
        item = self.tableInitPowders.verticalHeaderItem(9)
        item.setText(_translate("initWindow", "Κ1: "))
        item = self.tableInitPowders.verticalHeaderItem(10)
        item.setText(_translate("initWindow", "λ1: "))
        item = self.tableInitPowders.verticalHeaderItem(11)
        item.setText(_translate("initWindow", "μ1: "))
        item = self.tableInitPowders.verticalHeaderItem(12)
        item.setText(_translate("initWindow", "Κ2: "))
        item = self.tableInitPowders.verticalHeaderItem(13)
        item.setText(_translate("initWindow", "λ2: "))
        item = self.tableInitPowders.verticalHeaderItem(14)
        item.setText(_translate("initWindow", "μ2: "))
        self.butt_del.setText(_translate("initWindow", "Удалить..."))
        self.butt_add.setText(_translate("initWindow", "Добавить колонку"))
        self.groupBox_3.setTitle(_translate("initWindow", "Характеристики арт. системы:"))
        item = self.tableInitArtSys.verticalHeaderItem(0)
        item.setText(_translate("initWindow", "Орудие:"))
        item = self.tableInitArtSys.verticalHeaderItem(1)
        item.setText(_translate("initWindow", "Калибр d, м:"))
        item = self.tableInitArtSys.verticalHeaderItem(2)
        item.setText(_translate("initWindow", "Масса снаряда q, кг:"))
        item = self.tableInitArtSys.verticalHeaderItem(3)
        item.setText(_translate("initWindow", "Площадь сечения канала ствола S, м²: "))
        item = self.tableInitArtSys.verticalHeaderItem(4)
        item.setText(_translate("initWindow", "Объём зарядной каморы W₀, м³:"))
        item = self.tableInitArtSys.verticalHeaderItem(5)
        item.setText(_translate("initWindow", "Путь снаряда в канале ствола lд, м:"))
        item = self.tableInitArtSys.verticalHeaderItem(6)
        item.setText(_translate("initWindow", "Длина зарядной каморы lкм, м:"))
        item = self.tableInitArtSys.verticalHeaderItem(7)
        item.setText(_translate("initWindow", "Привед. длина зарядной каморы l₀, м:"))
        item = self.tableInitArtSys.verticalHeaderItem(8)
        item.setText(_translate("initWindow", "Коэффициент Слухоцкого kφ:"))
        __sortingEnabled = self.tableInitArtSys.isSortingEnabled()
        self.tableInitArtSys.setSortingEnabled(False)
        self.tableInitArtSys.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("initWindow", "Параметры заряжания:"))
        self.label_PressIgnit.setText(_translate("initWindow", "Давление воспламенителя, МПа:  "))
        self.label_PressForc.setText(_translate("initWindow", "Давление форсирования, МПа: "))
        self.bases.setTitle(_translate("initWindow", "Базы..."))
        self.file.setTitle(_translate("initWindow", "Файл"))
        self.menu.setTitle(_translate("initWindow", "Помощь"))
        self.act_powders.setText(_translate("initWindow", "Пороха"))
        self.act_artsys.setText(_translate("initWindow", "Арт. системы"))
        self.act_open.setText(_translate("initWindow", "Открыть.."))
        self.act_save.setText(_translate("initWindow", "Сохранить.."))
        self.action.setText(_translate("initWindow", "Тебе никто не поможет..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    initWindow = QtWidgets.QMainWindow()
    ui = Ui_initWindow()
    ui.setupUi(initWindow)
    initWindow.show()
    sys.exit(app.exec_())
