# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\denis\PycharmProjects\GitHubBallOptimiz\GUI\Optimize\optimiz.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OptimizeWindow(object):
    def setupUi(self, OptimizeWindow):
        OptimizeWindow.setObjectName("OptimizeWindow")
        OptimizeWindow.resize(897, 768)
        self.centralwidget = QtWidgets.QWidget(OptimizeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_lims2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_lims2.setFont(font)
        self.groupBox_lims2.setObjectName("groupBox_lims2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_lims2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.val_maxPress = QtWidgets.QLineEdit(self.groupBox_lims2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_maxPress.sizePolicy().hasHeightForWidth())
        self.val_maxPress.setSizePolicy(sizePolicy)
        self.val_maxPress.setMinimumSize(QtCore.QSize(0, 25))
        self.val_maxPress.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.val_maxPress.setFont(font)
        self.val_maxPress.setText("")
        self.val_maxPress.setAlignment(QtCore.Qt.AlignCenter)
        self.val_maxPress.setObjectName("val_maxPress")
        self.gridLayout_3.addWidget(self.val_maxPress, 0, 1, 1, 1)
        self.label_maxPress = QtWidgets.QLabel(self.groupBox_lims2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_maxPress.setFont(font)
        self.label_maxPress.setObjectName("label_maxPress")
        self.gridLayout_3.addWidget(self.label_maxPress, 0, 0, 1, 1)
        self.label_coordGor = QtWidgets.QLabel(self.groupBox_lims2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_coordGor.setFont(font)
        self.label_coordGor.setObjectName("label_coordGor")
        self.gridLayout_3.addWidget(self.label_coordGor, 1, 0, 1, 1)
        self.val__coordGor = QtWidgets.QLineEdit(self.groupBox_lims2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val__coordGor.sizePolicy().hasHeightForWidth())
        self.val__coordGor.setSizePolicy(sizePolicy)
        self.val__coordGor.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.val__coordGor.setFont(font)
        self.val__coordGor.setAlignment(QtCore.Qt.AlignCenter)
        self.val__coordGor.setObjectName("val__coordGor")
        self.gridLayout_3.addWidget(self.val__coordGor, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_lims2, 0, 1, 1, 1)
        self.groupBox_ParamOptimize = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_ParamOptimize.setFont(font)
        self.groupBox_ParamOptimize.setObjectName("groupBox_ParamOptimize")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_ParamOptimize)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox_SelComp = QtWidgets.QCheckBox(self.groupBox_ParamOptimize)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_SelComp.setFont(font)
        self.checkBox_SelComp.setObjectName("checkBox_SelComp")
        self.gridLayout_4.addWidget(self.checkBox_SelComp, 1, 0, 1, 1)
        self.butt_Start = QtWidgets.QPushButton(self.groupBox_ParamOptimize)
        self.butt_Start.setObjectName("butt_Start")
        self.gridLayout_4.addWidget(self.butt_Start, 1, 1, 1, 1)
        self.comboBox_MethOptimize = QtWidgets.QComboBox(self.groupBox_ParamOptimize)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_MethOptimize.setFont(font)
        self.comboBox_MethOptimize.setObjectName("comboBox_MethOptimize")
        self.comboBox_MethOptimize.addItem("")
        self.comboBox_MethOptimize.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_MethOptimize, 0, 1, 1, 1)
        self.label_MethOptimize = QtWidgets.QLabel(self.groupBox_ParamOptimize)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_MethOptimize.setFont(font)
        self.label_MethOptimize.setObjectName("label_MethOptimize")
        self.gridLayout_4.addWidget(self.label_MethOptimize, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_ParamOptimize, 1, 0, 1, 2)
        self.groupBox_listing = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_listing.setFont(font)
        self.groupBox_listing.setObjectName("groupBox_listing")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_listing)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_optimize = QtWidgets.QTextBrowser(self.groupBox_listing)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_optimize.setFont(font)
        self.textBrowser_optimize.setObjectName("textBrowser_optimize")
        self.verticalLayout.addWidget(self.textBrowser_optimize)
        self.gridLayout.addWidget(self.groupBox_listing, 2, 0, 1, 2)
        self.groupBox_lims1 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_lims1.setFont(font)
        self.groupBox_lims1.setObjectName("groupBox_lims1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_lims1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.val_maxDensity = QtWidgets.QLineEdit(self.groupBox_lims1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_maxDensity.sizePolicy().hasHeightForWidth())
        self.val_maxDensity.setSizePolicy(sizePolicy)
        self.val_maxDensity.setMinimumSize(QtCore.QSize(0, 25))
        self.val_maxDensity.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.val_maxDensity.setFont(font)
        self.val_maxDensity.setAlignment(QtCore.Qt.AlignCenter)
        self.val_maxDensity.setObjectName("val_maxDensity")
        self.gridLayout_2.addWidget(self.val_maxDensity, 1, 1, 1, 1)
        self.val_massPowd = QtWidgets.QLineEdit(self.groupBox_lims1)
        self.val_massPowd.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_massPowd.sizePolicy().hasHeightForWidth())
        self.val_massPowd.setSizePolicy(sizePolicy)
        self.val_massPowd.setMinimumSize(QtCore.QSize(0, 25))
        self.val_massPowd.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.val_massPowd.setFont(font)
        self.val_massPowd.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.val_massPowd.setAlignment(QtCore.Qt.AlignCenter)
        self.val_massPowd.setObjectName("val_massPowd")
        self.gridLayout_2.addWidget(self.val_massPowd, 2, 1, 1, 1)
        self.label_massPowd = QtWidgets.QLabel(self.groupBox_lims1)
        self.label_massPowd.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_massPowd.setFont(font)
        self.label_massPowd.setObjectName("label_massPowd")
        self.gridLayout_2.addWidget(self.label_massPowd, 2, 0, 1, 1)
        self.label_maxDensity = QtWidgets.QLabel(self.groupBox_lims1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_maxDensity.setFont(font)
        self.label_maxDensity.setObjectName("label_maxDensity")
        self.gridLayout_2.addWidget(self.label_maxDensity, 1, 0, 1, 1)
        self.label_FinitImpuls = QtWidgets.QLabel(self.groupBox_lims1)
        self.label_FinitImpuls.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_FinitImpuls.setFont(font)
        self.label_FinitImpuls.setObjectName("label_FinitImpuls")
        self.gridLayout_2.addWidget(self.label_FinitImpuls, 3, 0, 1, 1)
        self.val_FinitImpuls = QtWidgets.QLineEdit(self.groupBox_lims1)
        self.val_FinitImpuls.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_FinitImpuls.sizePolicy().hasHeightForWidth())
        self.val_FinitImpuls.setSizePolicy(sizePolicy)
        self.val_FinitImpuls.setMinimumSize(QtCore.QSize(0, 25))
        self.val_FinitImpuls.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.val_FinitImpuls.setFont(font)
        self.val_FinitImpuls.setAlignment(QtCore.Qt.AlignCenter)
        self.val_FinitImpuls.setObjectName("val_FinitImpuls")
        self.gridLayout_2.addWidget(self.val_FinitImpuls, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_lims1, 0, 0, 1, 1)
        OptimizeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OptimizeWindow)
        QtCore.QMetaObject.connectSlotsByName(OptimizeWindow)

    def retranslateUi(self, OptimizeWindow):
        _translate = QtCore.QCoreApplication.translate
        OptimizeWindow.setWindowTitle(_translate("OptimizeWindow", "Оптимизация баллистических параметров"))
        self.groupBox_lims2.setTitle(_translate("OptimizeWindow", "Вектор ограничений 2-го рода"))
        self.label_maxPress.setText(_translate("OptimizeWindow", "Максимальное давление, МПа:"))
        self.label_coordGor.setText(_translate("OptimizeWindow", "Относ. коорд. окончания горения (не более):"))
        self.groupBox_ParamOptimize.setTitle(_translate("OptimizeWindow", "Параметры оптимизации"))
        self.checkBox_SelComp.setText(_translate("OptimizeWindow", "Подобрать компоненты"))
        self.butt_Start.setText(_translate("OptimizeWindow", "Начать"))
        self.comboBox_MethOptimize.setItemText(0, _translate("OptimizeWindow", "Случайный поиск"))
        self.comboBox_MethOptimize.setItemText(1, _translate("OptimizeWindow", "Случайное сканирование"))
        self.label_MethOptimize.setText(_translate("OptimizeWindow", "Метод оптимизации:"))
        self.groupBox_listing.setTitle(_translate("OptimizeWindow", "Листинг"))
        self.textBrowser_optimize.setHtml(_translate("OptimizeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_lims1.setTitle(_translate("OptimizeWindow", "Вектор ограничений 1-го рода"))
        self.label_massPowd.setText(_translate("OptimizeWindow", "Масса пороховой навески, ±%:"))
        self.label_maxDensity.setText(_translate("OptimizeWindow", "Максимальная плотность заряжания, кг/м³:"))
        self.label_FinitImpuls.setText(_translate("OptimizeWindow", "Конечный импульс, ±%:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OptimizeWindow = QtWidgets.QMainWindow()
    ui = Ui_OptimizeWindow()
    ui.setupUi(OptimizeWindow)
    OptimizeWindow.show()
    sys.exit(app.exec_())
