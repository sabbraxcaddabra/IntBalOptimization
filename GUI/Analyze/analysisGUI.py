# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\denis\PycharmProjects\GitHubBallOptimiz\GUI\Analyze\analysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogRes(object):
    def setupUi(self, DialogRes):
        DialogRes.setObjectName("DialogRes")
        DialogRes.resize(970, 820)
        DialogRes.setMinimumSize(QtCore.QSize(970, 820))
        DialogRes.setMaximumSize(QtCore.QSize(970, 820))
        DialogRes.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.raschet_tab = QtWidgets.QTabWidget(DialogRes)
        self.raschet_tab.setGeometry(QtCore.QRect(10, 10, 950, 800))
        self.raschet_tab.setMinimumSize(QtCore.QSize(950, 800))
        self.raschet_tab.setMaximumSize(QtCore.QSize(950, 800))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.raschet_tab.setFont(font)
        self.raschet_tab.setInputMethodHints(QtCore.Qt.ImhNone)
        self.raschet_tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.raschet_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.raschet_tab.setObjectName("raschet_tab")
        self.calculation = QtWidgets.QWidget()
        self.calculation.setObjectName("calculation")
        self.groupBox = QtWidgets.QGroupBox(self.calculation)
        self.groupBox.setGeometry(QtCore.QRect(20, 190, 921, 571))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.result_table = QtWidgets.QTableWidget(self.groupBox)
        self.result_table.setGeometry(QtCore.QRect(10, 30, 902, 531))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.result_table.setFont(font)
        self.result_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.result_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.result_table.setProperty("showDropIndicator", True)
        self.result_table.setShowGrid(True)
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(7)
        self.result_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.result_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.result_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.result_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.result_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.result_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.result_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.result_table.setHorizontalHeaderItem(6, item)
        self.result_table.horizontalHeader().setDefaultSectionSize(122)
        self.result_table.horizontalHeader().setMinimumSectionSize(122)
        self.result_table.verticalHeader().setDefaultSectionSize(25)
        self.result_table.verticalHeader().setMinimumSectionSize(25)
        self.groupBox_2 = QtWidgets.QGroupBox(self.calculation)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 471, 171))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.method_comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.method_comboBox.setGeometry(QtCore.QRect(160, 30, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.method_comboBox.setFont(font)
        self.method_comboBox.setObjectName("method_comboBox")
        self.method_comboBox.addItem("")
        self.method_comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 121, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.step_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.step_lineEdit.setGeometry(QtCore.QRect(340, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.step_lineEdit.setFont(font)
        self.step_lineEdit.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.step_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.step_lineEdit.setObjectName("step_lineEdit")
        self.butt_raschet = QtWidgets.QPushButton(self.groupBox_2)
        self.butt_raschet.setGeometry(QtCore.QRect(10, 130, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.butt_raschet.setFont(font)
        self.butt_raschet.setObjectName("butt_raschet")
        self.groupBox_5 = QtWidgets.QGroupBox(self.calculation)
        self.groupBox_5.setGeometry(QtCore.QRect(500, 10, 441, 171))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.lineEdit_AverPress = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_AverPress.setGeometry(QtCore.QRect(330, 80, 101, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_AverPress.setFont(font)
        self.lineEdit_AverPress.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_AverPress.setReadOnly(True)
        self.lineEdit_AverPress.setObjectName("lineEdit_AverPress")
        self.label_GunSpeed = QtWidgets.QLabel(self.groupBox_5)
        self.label_GunSpeed.setGeometry(QtCore.QRect(10, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_GunSpeed.setFont(font)
        self.label_GunSpeed.setObjectName("label_GunSpeed")
        self.lineEdit_GunSpeed = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_GunSpeed.setGeometry(QtCore.QRect(330, 40, 101, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_GunSpeed.setFont(font)
        self.lineEdit_GunSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_GunSpeed.setReadOnly(True)
        self.lineEdit_GunSpeed.setObjectName("lineEdit_GunSpeed")
        self.label_AverPress = QtWidgets.QLabel(self.groupBox_5)
        self.label_AverPress.setGeometry(QtCore.QRect(10, 80, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_AverPress.setFont(font)
        self.label_AverPress.setObjectName("label_AverPress")
        self.raschet_tab.addTab(self.calculation, "")
        self.plots = QtWidgets.QWidget()
        self.plots.setObjectName("plots")
        self.groupBox_3 = QtWidgets.QGroupBox(self.plots)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 931, 761))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.plot_comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.plot_comboBox.setGeometry(QtCore.QRect(610, 30, 301, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.plot_comboBox.setFont(font)
        self.plot_comboBox.setObjectName("plot_comboBox")
        self.plot_comboBox.addItem("")
        self.plot_comboBox.addItem("")
        self.plot_comboBox.addItem("")
        self.plot_comboBox.addItem("")
        self.plot_comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 241, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 80, 911, 621))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 891, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.plot_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.plot_Layout.setContentsMargins(0, 0, 0, 0)
        self.plot_Layout.setObjectName("plot_Layout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(810, 710, 111, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.raschet_tab.addTab(self.plots, "")

        self.retranslateUi(DialogRes)
        self.raschet_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DialogRes)

    def retranslateUi(self, DialogRes):
        _translate = QtCore.QCoreApplication.translate
        DialogRes.setWindowTitle(_translate("DialogRes", "Анализ баллистических параметров"))
        self.groupBox.setTitle(_translate("DialogRes", "Листинг"))
        item = self.result_table.verticalHeaderItem(0)
        item.setText(_translate("DialogRes", "1"))
        item = self.result_table.horizontalHeaderItem(0)
        item.setText(_translate("DialogRes", "t, мc"))
        item = self.result_table.horizontalHeaderItem(1)
        item.setText(_translate("DialogRes", "V, м/с"))
        item = self.result_table.horizontalHeaderItem(2)
        item.setText(_translate("DialogRes", "L, м"))
        item = self.result_table.horizontalHeaderItem(3)
        item.setText(_translate("DialogRes", "Ψ"))
        item = self.result_table.horizontalHeaderItem(4)
        item.setText(_translate("DialogRes", "P, МПа"))
        item = self.result_table.horizontalHeaderItem(5)
        item.setText(_translate("DialogRes", "Pсн, МПа"))
        item = self.result_table.horizontalHeaderItem(6)
        item.setText(_translate("DialogRes", "Pкн, МПа"))
        self.groupBox_2.setTitle(_translate("DialogRes", "Укажите параметры выполнения расчёта"))
        self.label.setText(_translate("DialogRes", "Метод расчета:"))
        self.method_comboBox.setItemText(0, _translate("DialogRes", "Метод Рунге-Кутты 4-го порядка"))
        self.method_comboBox.setItemText(1, _translate("DialogRes", "Метод Адамса-Башфорда 5-го порядка"))
        self.label_2.setText(_translate("DialogRes", "Шаг расчета, c: "))
        self.step_lineEdit.setText(_translate("DialogRes", "1E-5"))
        self.butt_raschet.setText(_translate("DialogRes", "Расчёт"))
        self.groupBox_5.setTitle(_translate("DialogRes", "Основные результаты расчёта"))
        self.label_GunSpeed.setText(_translate("DialogRes", "Дульная скорость, м/с: "))
        self.label_AverPress.setText(_translate("DialogRes", "Максимальное среднебалл. давление, МПа:"))
        self.raschet_tab.setTabText(self.raschet_tab.indexOf(self.calculation), _translate("DialogRes", "Расчет"))
        self.groupBox_3.setTitle(_translate("DialogRes", "Построение графиков"))
        self.plot_comboBox.setItemText(0, _translate("DialogRes", "<не указан>"))
        self.plot_comboBox.setItemText(1, _translate("DialogRes", "Среднебаллистическое давление"))
        self.plot_comboBox.setItemText(2, _translate("DialogRes", "Давление на дно снаряда"))
        self.plot_comboBox.setItemText(3, _translate("DialogRes", "Давление на дно канала ствола"))
        self.plot_comboBox.setItemText(4, _translate("DialogRes", "Скорость"))
        self.label_4.setText(_translate("DialogRes", "Выберите график для построения:"))
        self.pushButton.setText(_translate("DialogRes", "Закрыть"))
        self.raschet_tab.setTabText(self.raschet_tab.indexOf(self.plots), _translate("DialogRes", "График"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogRes = QtWidgets.QDialog()
    ui = Ui_DialogRes()
    ui.setupUi(DialogRes)
    DialogRes.show()
    sys.exit(app.exec_())
