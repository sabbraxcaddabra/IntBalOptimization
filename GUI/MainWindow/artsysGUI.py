# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\denis\PycharmProjects\GitHubBallOptimiz\GUI\MainWindow\artsys.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogArtSys(object):
    def setupUi(self, DialogArtSys):
        DialogArtSys.setObjectName("DialogArtSys")
        DialogArtSys.resize(723, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogArtSys.sizePolicy().hasHeightForWidth())
        DialogArtSys.setSizePolicy(sizePolicy)
        DialogArtSys.setMinimumSize(QtCore.QSize(723, 500))
        DialogArtSys.setMaximumSize(QtCore.QSize(723, 500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        DialogArtSys.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        DialogArtSys.setFont(font)
        self.tableCharArtSys = QtWidgets.QTableWidget(DialogArtSys)
        self.tableCharArtSys.setGeometry(QtCore.QRect(10, 10, 701, 441))
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
        self.butt_ArtSysAdd = QtWidgets.QPushButton(DialogArtSys)
        self.butt_ArtSysAdd.setGeometry(QtCore.QRect(630, 460, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.butt_ArtSysAdd.setFont(font)
        self.butt_ArtSysAdd.setObjectName("butt_ArtSysAdd")
        self.butt_ArtSysClose = QtWidgets.QPushButton(DialogArtSys)
        self.butt_ArtSysClose.setGeometry(QtCore.QRect(540, 460, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.butt_ArtSysClose.setFont(font)
        self.butt_ArtSysClose.setObjectName("butt_ArtSysClose")

        self.retranslateUi(DialogArtSys)
        QtCore.QMetaObject.connectSlotsByName(DialogArtSys)

    def retranslateUi(self, DialogArtSys):
        _translate = QtCore.QCoreApplication.translate
        DialogArtSys.setWindowTitle(_translate("DialogArtSys", "Характеристики арт. систем"))
        item = self.tableCharArtSys.verticalHeaderItem(0)
        item.setText(_translate("DialogArtSys", "1"))
        item = self.tableCharArtSys.horizontalHeaderItem(0)
        item.setText(_translate("DialogArtSys", "Орудие"))
        item = self.tableCharArtSys.horizontalHeaderItem(1)
        item.setText(_translate("DialogArtSys", "d, м"))
        item = self.tableCharArtSys.horizontalHeaderItem(2)
        item.setText(_translate("DialogArtSys", "S, м²"))
        item = self.tableCharArtSys.horizontalHeaderItem(3)
        item.setText(_translate("DialogArtSys", "W₀ , м³"))
        item = self.tableCharArtSys.horizontalHeaderItem(4)
        item.setText(_translate("DialogArtSys", "lд, м"))
        item = self.tableCharArtSys.horizontalHeaderItem(5)
        item.setText(_translate("DialogArtSys", "lкм, м"))
        item = self.tableCharArtSys.horizontalHeaderItem(6)
        item.setText(_translate("DialogArtSys", "l₀ , м"))
        item = self.tableCharArtSys.horizontalHeaderItem(7)
        item.setText(_translate("DialogArtSys", "kφ"))
        __sortingEnabled = self.tableCharArtSys.isSortingEnabled()
        self.tableCharArtSys.setSortingEnabled(False)
        self.tableCharArtSys.setSortingEnabled(__sortingEnabled)
        self.butt_ArtSysAdd.setText(_translate("DialogArtSys", "Добавить"))
        self.butt_ArtSysClose.setText(_translate("DialogArtSys", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogArtSys = QtWidgets.QDialog()
    ui = Ui_DialogArtSys()
    ui.setupUi(DialogArtSys)
    DialogArtSys.show()
    sys.exit(app.exec_())
