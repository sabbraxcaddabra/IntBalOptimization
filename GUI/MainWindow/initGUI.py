# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\denis\PycharmProjects\GitHubBallOptimiz\GUI\MainWindow\init.ui'
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
        initWindow.resize(794, 665)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(initWindow.sizePolicy().hasHeightForWidth())
        initWindow.setSizePolicy(sizePolicy)
        initWindow.setMinimumSize(QtCore.QSize(0, 665))
        initWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        initWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        initWindow.setFont(font)
        initWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.centralwidget = QtWidgets.QWidget(initWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableInitArtSys = QtWidgets.QTableWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableInitArtSys.sizePolicy().hasHeightForWidth())
        self.tableInitArtSys.setSizePolicy(sizePolicy)
        self.tableInitArtSys.setMinimumSize(QtCore.QSize(425, 272))
        self.tableInitArtSys.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tableInitArtSys.setFont(font)
        self.tableInitArtSys.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableInitArtSys.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableInitArtSys.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableInitArtSys.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableInitArtSys.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableInitArtSys.setAutoScrollMargin(10)
        self.tableInitArtSys.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
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
        self.tableInitArtSys.horizontalHeader().setCascadingSectionResizes(False)
        self.tableInitArtSys.horizontalHeader().setDefaultSectionSize(150)
        self.tableInitArtSys.horizontalHeader().setHighlightSections(True)
        self.tableInitArtSys.horizontalHeader().setMinimumSectionSize(30)
        self.tableInitArtSys.verticalHeader().setVisible(True)
        self.tableInitArtSys.verticalHeader().setCascadingSectionResizes(False)
        self.tableInitArtSys.verticalHeader().setDefaultSectionSize(30)
        self.tableInitArtSys.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_3.addWidget(self.tableInitArtSys)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_regIgnit = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_regIgnit.setFont(font)
        self.label_regIgnit.setObjectName("label_regIgnit")
        self.verticalLayout_6.addWidget(self.label_regIgnit)
        self.label_PressIgnit = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_PressIgnit.setFont(font)
        self.label_PressIgnit.setObjectName("label_PressIgnit")
        self.verticalLayout_6.addWidget(self.label_PressIgnit)
        self.label_PressForc = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_PressForc.setFont(font)
        self.label_PressForc.setObjectName("label_PressForc")
        self.verticalLayout_6.addWidget(self.label_PressForc)
        self.label_Temp = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_Temp.setFont(font)
        self.label_Temp.setObjectName("label_Temp")
        self.verticalLayout_6.addWidget(self.label_Temp)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.combo_regIgnit = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_regIgnit.sizePolicy().hasHeightForWidth())
        self.combo_regIgnit.setSizePolicy(sizePolicy)
        self.combo_regIgnit.setMinimumSize(QtCore.QSize(0, 0))
        self.combo_regIgnit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.combo_regIgnit.setFont(font)
        self.combo_regIgnit.setObjectName("combo_regIgnit")
        self.combo_regIgnit.addItem("")
        self.combo_regIgnit.addItem("")
        self.verticalLayout_5.addWidget(self.combo_regIgnit)
        self.val_PressIgnit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_PressIgnit.sizePolicy().hasHeightForWidth())
        self.val_PressIgnit.setSizePolicy(sizePolicy)
        self.val_PressIgnit.setMinimumSize(QtCore.QSize(0, 0))
        self.val_PressIgnit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.val_PressIgnit.setFont(font)
        self.val_PressIgnit.setText("")
        self.val_PressIgnit.setMaxLength(11)
        self.val_PressIgnit.setAlignment(QtCore.Qt.AlignCenter)
        self.val_PressIgnit.setObjectName("val_PressIgnit")
        self.verticalLayout_5.addWidget(self.val_PressIgnit)
        self.val_PressForc = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_PressForc.sizePolicy().hasHeightForWidth())
        self.val_PressForc.setSizePolicy(sizePolicy)
        self.val_PressForc.setMinimumSize(QtCore.QSize(0, 0))
        self.val_PressForc.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.val_PressForc.setFont(font)
        self.val_PressForc.setText("")
        self.val_PressForc.setMaxLength(11)
        self.val_PressForc.setAlignment(QtCore.Qt.AlignCenter)
        self.val_PressForc.setObjectName("val_PressForc")
        self.verticalLayout_5.addWidget(self.val_PressForc)
        self.val_Temp = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.val_Temp.sizePolicy().hasHeightForWidth())
        self.val_Temp.setSizePolicy(sizePolicy)
        self.val_Temp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.val_Temp.setFont(font)
        self.val_Temp.setText("")
        self.val_Temp.setMaxLength(11)
        self.val_Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.val_Temp.setObjectName("val_Temp")
        self.verticalLayout_5.addWidget(self.val_Temp)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.butt_anal = QtWidgets.QPushButton(self.centralwidget)
        self.butt_anal.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.butt_anal.setFont(font)
        self.butt_anal.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.butt_anal.setObjectName("butt_anal")
        self.horizontalLayout_6.addWidget(self.butt_anal)
        self.butt_synth = QtWidgets.QPushButton(self.centralwidget)
        self.butt_synth.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.butt_synth.setFont(font)
        self.butt_synth.setObjectName("butt_synth")
        self.horizontalLayout_6.addWidget(self.butt_synth)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableInitPowders = QtWidgets.QTableWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableInitPowders.sizePolicy().hasHeightForWidth())
        self.tableInitPowders.setSizePolicy(sizePolicy)
        self.tableInitPowders.setMinimumSize(QtCore.QSize(303, 448))
        self.tableInitPowders.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tableInitPowders.setFont(font)
        self.tableInitPowders.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableInitPowders.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableInitPowders.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableInitPowders.setAutoScrollMargin(10)
        self.tableInitPowders.setAlternatingRowColors(False)
        self.tableInitPowders.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableInitPowders.setObjectName("tableInitPowders")
        self.tableInitPowders.setColumnCount(0)
        self.tableInitPowders.setRowCount(17)
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
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableInitPowders.setVerticalHeaderItem(16, item)
        self.tableInitPowders.horizontalHeader().setVisible(True)
        self.tableInitPowders.verticalHeader().setVisible(True)
        self.tableInitPowders.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.tableInitPowders)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.butt_del = QtWidgets.QPushButton(self.groupBox_2)
        self.butt_del.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.butt_del.setFont(font)
        self.butt_del.setObjectName("butt_del")
        self.horizontalLayout.addWidget(self.butt_del)
        self.butt_add = QtWidgets.QPushButton(self.groupBox_2)
        self.butt_add.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.butt_add.setFont(font)
        self.butt_add.setAutoDefault(False)
        self.butt_add.setObjectName("butt_add")
        self.horizontalLayout.addWidget(self.butt_add)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        initWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(initWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 23))
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
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.bases.menuAction())

        self.retranslateUi(initWindow)
        QtCore.QMetaObject.connectSlotsByName(initWindow)

    def retranslateUi(self, initWindow):
        _translate = QtCore.QCoreApplication.translate
        initWindow.setWindowTitle(_translate("initWindow", "Программа кафедры Е3 - BallOptimize"))
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
        self.label_regIgnit.setText(_translate("initWindow", "Учёт воспламенителя:"))
        self.label_PressIgnit.setText(_translate("initWindow", "Давление воспламенителя, МПа:  "))
        self.label_PressForc.setText(_translate("initWindow", "Давление форсирования, МПа: "))
        self.label_Temp.setText(_translate("initWindow", "Темп. метатательного заряда, °С: "))
        self.combo_regIgnit.setItemText(0, _translate("initWindow", "Давление"))
        self.combo_regIgnit.setItemText(1, _translate("initWindow", "Масса"))
        self.butt_anal.setText(_translate("initWindow", "Анализ"))
        self.butt_synth.setText(_translate("initWindow", "Синтез"))
        self.groupBox_2.setTitle(_translate("initWindow", "Характеристики метательного заряда:"))
        item = self.tableInitPowders.verticalHeaderItem(0)
        item.setText(_translate("initWindow", "Марка пороха: "))
        item = self.tableInitPowders.verticalHeaderItem(1)
        item.setText(_translate("initWindow", "ω, кг: "))
        item = self.tableInitPowders.verticalHeaderItem(2)
        item.setText(_translate("initWindow", "δ, кг/м³: "))
        item = self.tableInitPowders.verticalHeaderItem(3)
        item.setText(_translate("initWindow", "f, Дж/кг: "))
        item = self.tableInitPowders.verticalHeaderItem(4)
        item.setText(_translate("initWindow", "T₁, К: "))
        item = self.tableInitPowders.verticalHeaderItem(5)
        item.setText(_translate("initWindow", "Iк, Па⋅с: "))
        item = self.tableInitPowders.verticalHeaderItem(6)
        item.setText(_translate("initWindow", "α, м³/кг: "))
        item = self.tableInitPowders.verticalHeaderItem(7)
        item.setText(_translate("initWindow", "θ: "))
        item = self.tableInitPowders.verticalHeaderItem(8)
        item.setText(_translate("initWindow", "Zк: "))
        item = self.tableInitPowders.verticalHeaderItem(9)
        item.setText(_translate("initWindow", "Κ₁: "))
        item = self.tableInitPowders.verticalHeaderItem(10)
        item.setText(_translate("initWindow", "λ₁: "))
        item = self.tableInitPowders.verticalHeaderItem(11)
        item.setText(_translate("initWindow", "μ₁: "))
        item = self.tableInitPowders.verticalHeaderItem(12)
        item.setText(_translate("initWindow", "Κ₂: "))
        item = self.tableInitPowders.verticalHeaderItem(13)
        item.setText(_translate("initWindow", "λ₂: "))
        item = self.tableInitPowders.verticalHeaderItem(14)
        item.setText(_translate("initWindow", "μ₂: "))
        item = self.tableInitPowders.verticalHeaderItem(15)
        item.setText(_translate("initWindow", "KfT"))
        item = self.tableInitPowders.verticalHeaderItem(16)
        item.setText(_translate("initWindow", "KJt"))
        self.butt_del.setText(_translate("initWindow", "Удалить..."))
        self.butt_add.setText(_translate("initWindow", "Добавить колонку"))
        self.bases.setTitle(_translate("initWindow", "Базы..."))
        self.file.setTitle(_translate("initWindow", "Файл"))
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