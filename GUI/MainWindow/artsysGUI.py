# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\denis\PycharmProjects\GitHubBallOptimiz\GUI\MainWindow\artsys.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ArtSysWindow(object):
    def setupUi(self, ArtSysWindow):
        ArtSysWindow.setObjectName("ArtSysWindow")
        ArtSysWindow.resize(679, 520)
        self.centralwidget = QtWidgets.QWidget(ArtSysWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableCharArtSys = QtWidgets.QTableWidget(self.centralwidget)
        self.tableCharArtSys.setMaximumSize(QtCore.QSize(16777211, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tableCharArtSys.setFont(font)
        self.tableCharArtSys.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableCharArtSys.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableCharArtSys.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableCharArtSys.setColumnCount(8)
        self.tableCharArtSys.setObjectName("tableCharArtSys")
        self.tableCharArtSys.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharArtSys.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCharArtSys.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCharArtSys.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCharArtSys.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCharArtSys.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCharArtSys.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCharArtSys.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCharArtSys.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCharArtSys.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableCharArtSys.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableCharArtSys.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableCharArtSys.setItem(0, 2, item)
        self.tableCharArtSys.horizontalHeader().setCascadingSectionResizes(False)
        self.tableCharArtSys.horizontalHeader().setDefaultSectionSize(75)
        self.tableCharArtSys.horizontalHeader().setMinimumSectionSize(80)
        self.tableCharArtSys.verticalHeader().setCascadingSectionResizes(False)
        self.tableCharArtSys.verticalHeader().setDefaultSectionSize(30)
        self.tableCharArtSys.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.tableCharArtSys)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.butt_ArtSysClose = QtWidgets.QPushButton(self.centralwidget)
        self.butt_ArtSysClose.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.butt_ArtSysClose.setFont(font)
        self.butt_ArtSysClose.setObjectName("butt_ArtSysClose")
        self.horizontalLayout.addWidget(self.butt_ArtSysClose)
        self.butt_ArtSysAdd = QtWidgets.QPushButton(self.centralwidget)
        self.butt_ArtSysAdd.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.butt_ArtSysAdd.setFont(font)
        self.butt_ArtSysAdd.setObjectName("butt_ArtSysAdd")
        self.horizontalLayout.addWidget(self.butt_ArtSysAdd)
        self.verticalLayout.addLayout(self.horizontalLayout)
        ArtSysWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ArtSysWindow)
        QtCore.QMetaObject.connectSlotsByName(ArtSysWindow)

    def retranslateUi(self, ArtSysWindow):
        _translate = QtCore.QCoreApplication.translate
        ArtSysWindow.setWindowTitle(_translate("ArtSysWindow", "База арт. систем"))
        item = self.tableCharArtSys.verticalHeaderItem(0)
        item.setText(_translate("ArtSysWindow", "1"))
        item = self.tableCharArtSys.horizontalHeaderItem(0)
        item.setText(_translate("ArtSysWindow", "Орудие"))
        item = self.tableCharArtSys.horizontalHeaderItem(1)
        item.setText(_translate("ArtSysWindow", "d, м"))
        item = self.tableCharArtSys.horizontalHeaderItem(2)
        item.setText(_translate("ArtSysWindow", "S, м²"))
        item = self.tableCharArtSys.horizontalHeaderItem(3)
        item.setText(_translate("ArtSysWindow", "W₀ , м³"))
        item = self.tableCharArtSys.horizontalHeaderItem(4)
        item.setText(_translate("ArtSysWindow", "lд, м"))
        item = self.tableCharArtSys.horizontalHeaderItem(5)
        item.setText(_translate("ArtSysWindow", "lкм, м"))
        item = self.tableCharArtSys.horizontalHeaderItem(6)
        item.setText(_translate("ArtSysWindow", "l₀ , м"))
        item = self.tableCharArtSys.horizontalHeaderItem(7)
        item.setText(_translate("ArtSysWindow", "kφ"))
        __sortingEnabled = self.tableCharArtSys.isSortingEnabled()
        self.tableCharArtSys.setSortingEnabled(False)
        self.tableCharArtSys.setSortingEnabled(__sortingEnabled)
        self.butt_ArtSysClose.setText(_translate("ArtSysWindow", "Закрыть"))
        self.butt_ArtSysAdd.setText(_translate("ArtSysWindow", "Добавить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ArtSysWindow = QtWidgets.QMainWindow()
    ui = Ui_ArtSysWindow()
    ui.setupUi(ArtSysWindow)
    ArtSysWindow.show()
    sys.exit(app.exec_())
