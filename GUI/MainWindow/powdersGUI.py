# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\denis\PycharmProjects\BallOptimiz\powders.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogPowders(object):
    def setupUi(self, DialogPowders):
        DialogPowders.setObjectName("DialogPowders")
        DialogPowders.resize(1193, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogPowders.sizePolicy().hasHeightForWidth())
        DialogPowders.setSizePolicy(sizePolicy)
        DialogPowders.setMinimumSize(QtCore.QSize(1193, 500))
        DialogPowders.setMaximumSize(QtCore.QSize(1193, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        DialogPowders.setFont(font)
        self.tableCharPowders = QtWidgets.QTableWidget(DialogPowders)
        self.tableCharPowders.setGeometry(QtCore.QRect(10, 10, 1172, 441))
        self.tableCharPowders.setMaximumSize(QtCore.QSize(16777211, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableCharPowders.setFont(font)
        self.tableCharPowders.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableCharPowders.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableCharPowders.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableCharPowders.setColumnCount(14)
        self.tableCharPowders.setObjectName("tableCharPowders")
        self.tableCharPowders.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCharPowders.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableCharPowders.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableCharPowders.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableCharPowders.setItem(0, 2, item)
        self.tableCharPowders.horizontalHeader().setCascadingSectionResizes(False)
        self.tableCharPowders.horizontalHeader().setDefaultSectionSize(75)
        self.tableCharPowders.horizontalHeader().setMinimumSectionSize(80)
        self.tableCharPowders.verticalHeader().setCascadingSectionResizes(False)
        self.tableCharPowders.verticalHeader().setDefaultSectionSize(30)
        self.tableCharPowders.verticalHeader().setMinimumSectionSize(30)
        self.butt_PowdersAdd = QtWidgets.QPushButton(DialogPowders)
        self.butt_PowdersAdd.setGeometry(QtCore.QRect(1100, 460, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.butt_PowdersAdd.setFont(font)
        self.butt_PowdersAdd.setObjectName("butt_PowdersAdd")
        self.butt_PowdersClose = QtWidgets.QPushButton(DialogPowders)
        self.butt_PowdersClose.setGeometry(QtCore.QRect(1010, 460, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.butt_PowdersClose.setFont(font)
        self.butt_PowdersClose.setObjectName("butt_PowdersClose")

        self.retranslateUi(DialogPowders)
        QtCore.QMetaObject.connectSlotsByName(DialogPowders)

    def retranslateUi(self, DialogPowders):
        _translate = QtCore.QCoreApplication.translate
        DialogPowders.setWindowTitle(_translate("DialogPowders", "Характеристики порохов"))
        item = self.tableCharPowders.verticalHeaderItem(0)
        item.setText(_translate("DialogPowders", "1"))
        item = self.tableCharPowders.horizontalHeaderItem(0)
        item.setText(_translate("DialogPowders", "Марка"))
        item = self.tableCharPowders.horizontalHeaderItem(1)
        item.setText(_translate("DialogPowders", "Delta, кг/м³"))
        item = self.tableCharPowders.horizontalHeaderItem(2)
        item.setText(_translate("DialogPowders", "f, Дж/кг"))
        item = self.tableCharPowders.horizontalHeaderItem(3)
        item.setText(_translate("DialogPowders", "T1, К"))
        item = self.tableCharPowders.horizontalHeaderItem(4)
        item.setText(_translate("DialogPowders", "Iк, Па⋅с"))
        item = self.tableCharPowders.horizontalHeaderItem(5)
        item.setText(_translate("DialogPowders", "α, м³/кг"))
        item = self.tableCharPowders.horizontalHeaderItem(6)
        item.setText(_translate("DialogPowders", "θ"))
        item = self.tableCharPowders.horizontalHeaderItem(7)
        item.setText(_translate("DialogPowders", "Zк"))
        item = self.tableCharPowders.horizontalHeaderItem(8)
        item.setText(_translate("DialogPowders", "Κ1"))
        item = self.tableCharPowders.horizontalHeaderItem(9)
        item.setText(_translate("DialogPowders", "λ1"))
        item = self.tableCharPowders.horizontalHeaderItem(10)
        item.setText(_translate("DialogPowders", "μ1"))
        item = self.tableCharPowders.horizontalHeaderItem(11)
        item.setText(_translate("DialogPowders", "Κ2"))
        item = self.tableCharPowders.horizontalHeaderItem(12)
        item.setText(_translate("DialogPowders", "λ2"))
        item = self.tableCharPowders.horizontalHeaderItem(13)
        item.setText(_translate("DialogPowders", "μ2"))
        __sortingEnabled = self.tableCharPowders.isSortingEnabled()
        self.tableCharPowders.setSortingEnabled(False)
        self.tableCharPowders.setSortingEnabled(__sortingEnabled)
        self.butt_PowdersAdd.setText(_translate("DialogPowders", "Добавить"))
        self.butt_PowdersClose.setText(_translate("DialogPowders", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogPowders = QtWidgets.QDialog()
    ui = Ui_DialogPowders()
    ui.setupUi(DialogPowders)
    DialogPowders.show()
    sys.exit(app.exec_())
