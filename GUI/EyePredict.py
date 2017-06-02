# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TabsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from GUI.GuiLogic import GuiLogic


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1450, 1052)
        MainWindow.setStyleSheet("background-color: white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(-1, -6, 1451, 981))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("QTabBar::tab { font: 75 12pt \"Segoe Print\"; height: 70px; width: 300px;}\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.StartTab = QtWidgets.QWidget()
        self.StartTab.setEnabled(True)
        self.StartTab.setObjectName("StartTab")
        self.widget = QtWidgets.QWidget(self.StartTab)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(280, 22, 911, 881))
        self.widget.setObjectName("widget")
        self.greenLine = QtWidgets.QWidget(self.widget)
        self.greenLine.setEnabled(True)
        self.greenLine.setGeometry(QtCore.QRect(0, 641, 941, 80))
        self.greenLine.setStyleSheet("background-color: rgb(20, 179, 125)")
        self.greenLine.setObjectName("greenLine")
        self.TobeginText = QtWidgets.QLabel(self.widget)
        self.TobeginText.setEnabled(True)
        self.TobeginText.setGeometry(QtCore.QRect(90, 621, 781, 111))
        self.TobeginText.setStyleSheet("font: -10 20pt \"Segoe Print\";\n"
"color: rgb(245, 244, 255);\n"
"background: transparent;\n"
"")
        self.TobeginText.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TobeginText.setObjectName("TobeginText")
        self.BrowseButton = QtWidgets.QPushButton(self.widget)
        self.logic = GuiLogic(8)
        self.BrowseButton.clicked.connect(self.logic.Browse_Button_clicked)
        self.BrowseButton.setEnabled(True)
        self.BrowseButton.setGeometry(QtCore.QRect(300, 741, 311, 111))
        self.BrowseButton.setStyleSheet("font: -35 12pt \"Tahoma\";\n"
"border-style: outset;\n"
"    border-width: 3.5px;\n"
"    border-radius: 25px;\n"
"    border-color:rgb(51, 99, 111);\n"
"background-color:rgb(245, 244, 255)")
        self.BrowseButton.setObjectName("BrowseButton")
        self.Logo = QtWidgets.QLabel(self.widget)
        self.Logo.setEnabled(True)
        self.Logo.setGeometry(QtCore.QRect(-40, -70, 981, 701))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap(":/newPrefix/לוגו.jpg"))
        self.Logo.setObjectName("Logo")
        self.BlueLine = QtWidgets.QWidget(self.widget)
        self.BlueLine.setEnabled(True)
        self.BlueLine.setGeometry(QtCore.QRect(0, 721, 941, 80))
        self.BlueLine.setStyleSheet("background-color:rgb(35, 157, 158)")
        self.BlueLine.setObjectName("BlueLine")
        self.DarkLine = QtWidgets.QWidget(self.widget)
        self.DarkLine.setEnabled(True)
        self.DarkLine.setGeometry(QtCore.QRect(-10, 801, 941, 80))
        self.DarkLine.setStyleSheet("background-color: rgb(47, 110, 117)")
        self.DarkLine.setObjectName("DarkLine")
        self.blackLine = QtWidgets.QWidget(self.widget)
        self.blackLine.setEnabled(True)
        self.blackLine.setGeometry(QtCore.QRect(0, 637, 941, 16))
        self.blackLine.setStyleSheet("background-color: black")
        self.blackLine.setObjectName("blackLine")
        self.BlueLine.raise_()
        self.DarkLine.raise_()
        self.blackLine.raise_()
        self.greenLine.raise_()
        self.TobeginText.raise_()
        self.BrowseButton.raise_()
        self.Logo.raise_()
        self.BlackBackground = QtWidgets.QLabel(self.StartTab)
        self.BlackBackground.setEnabled(True)
        self.BlackBackground.setGeometry(QtCore.QRect(-10, 20, 1501, 891))
        self.BlackBackground.setStyleSheet("background: black")
        self.BlackBackground.setObjectName("BlackBackground")
        self.RDarkGreyLine = QtWidgets.QLabel(self.StartTab)
        self.RDarkGreyLine.setEnabled(True)
        self.RDarkGreyLine.setGeometry(QtCore.QRect(90, 24, 89, 881))
        self.RDarkGreyLine.setStyleSheet("background: rgb(154, 154, 154)")
        self.RDarkGreyLine.setText("")
        self.RDarkGreyLine.setObjectName("RDarkGreyLine")
        self.RLightGreyLine = QtWidgets.QLabel(self.StartTab)
        self.RLightGreyLine.setEnabled(True)
        self.RLightGreyLine.setGeometry(QtCore.QRect(185, 24, 89, 881))
        self.RLightGreyLine.setStyleSheet("background: rgb(224, 224, 224)")
        self.RLightGreyLine.setText("")
        self.RLightGreyLine.setObjectName("RLightGreyLine")
        self.LDarkGreyLine = QtWidgets.QLabel(self.StartTab)
        self.LDarkGreyLine.setEnabled(True)
        self.LDarkGreyLine.setGeometry(QtCore.QRect(1290, 23, 89, 881))
        self.LDarkGreyLine.setStyleSheet("background: rgb(154, 154, 154)")
        self.LDarkGreyLine.setText("")
        self.LDarkGreyLine.setObjectName("LDarkGreyLine")
        self.LLightGreyLine = QtWidgets.QLabel(self.StartTab)
        self.LLightGreyLine.setEnabled(True)
        self.LLightGreyLine.setGeometry(QtCore.QRect(1196, 23, 89, 881))
        self.LLightGreyLine.setStyleSheet("background: rgb(224, 224, 224)")
        self.LLightGreyLine.setText("")
        self.LLightGreyLine.setObjectName("LLightGreyLine")
        self.BlackBackground.raise_()
        self.widget.raise_()
        self.RDarkGreyLine.raise_()
        self.RLightGreyLine.raise_()
        self.LDarkGreyLine.raise_()
        self.LLightGreyLine.raise_()
        self.tabWidget.addTab(self.StartTab, "")
        self.DataTab = QtWidgets.QWidget()
        self.DataTab.setObjectName("DataTab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.DataTab)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 50, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, -1, 800, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Datalabel = QtWidgets.QLabel(self.DataTab)
        self.Datalabel.setStyleSheet("font: -10 11pt \"Tahoma\";    ")
        self.Datalabel.setObjectName("Datalabel")
        self.horizontalLayout_6.addWidget(self.Datalabel)
        self.ReloadButton = QtWidgets.QPushButton(self.DataTab)
        self.ReloadButton.setObjectName("ReloadButton")
        self.horizontalLayout_6.addWidget(self.ReloadButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.DataTable = QtWidgets.QTableWidget(self.DataTab)
        self.DataTable.setObjectName("DataTable")
        self.DataTable.setColumnCount(3)
        self.DataTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.DataTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.DataTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DataTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DataTable.setItem(0, 2, item)
        self.verticalLayout_3.addWidget(self.DataTable)
        self.line = QtWidgets.QFrame(self.DataTab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, 500, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.CurrentConfigurationLable = QtWidgets.QLabel(self.DataTab)
        self.CurrentConfigurationLable.setStyleSheet("font: -10 11pt \"Tahoma\";")
        self.CurrentConfigurationLable.setObjectName("CurrentConfigurationLable")
        self.horizontalLayout_5.addWidget(self.CurrentConfigurationLable)
        self.LoadButton = QtWidgets.QPushButton(self.DataTab)
        self.LoadButton.setObjectName("LoadButton")
        self.horizontalLayout_5.addWidget(self.LoadButton)
        self.SaveButton = QtWidgets.QPushButton(self.DataTab)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout_5.addWidget(self.SaveButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.ConfigurationTextEdit = QtWidgets.QTextEdit(self.DataTab)
        self.ConfigurationTextEdit.setObjectName("ConfigurationTextEdit")
        self.verticalLayout_3.addWidget(self.ConfigurationTextEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.DataTab, "")
        self.VisualizeTab = QtWidgets.QWidget()
        self.VisualizeTab.setObjectName("VisualizeTab")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.VisualizeTab)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ButtonsLayout = QtWidgets.QVBoxLayout()
        self.ButtonsLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.ButtonsLayout.setContentsMargins(25, 25, 25, 25)
        self.ButtonsLayout.setSpacing(5)
        self.ButtonsLayout.setObjectName("ButtonsLayout")
        self.HeatmapButton = QtWidgets.QPushButton(self.VisualizeTab)
        self.HeatmapButton.setMinimumSize(QtCore.QSize(250, 100))
        self.HeatmapButton.setStyleSheet("font: 11pt \"Tahoma\";\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(51, 99, 111);\n"
"background-color:rgb(245, 244, 255)")
        self.HeatmapButton.setDefault(False)
        self.HeatmapButton.setFlat(False)
        self.HeatmapButton.setObjectName("HeatmapButton")
        self.ButtonsLayout.addWidget(self.HeatmapButton)
        self.SaccadeTraceButton = QtWidgets.QPushButton(self.VisualizeTab)
        self.SaccadeTraceButton.setMinimumSize(QtCore.QSize(250, 100))
        self.SaccadeTraceButton.setStyleSheet("font: 11pt \"Tahoma\";\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color:rgb(51, 99, 111);\n"
"background-color:rgb(245, 244, 255)")
        self.SaccadeTraceButton.setObjectName("SaccadeTraceButton")
        self.ButtonsLayout.addWidget(self.SaccadeTraceButton)
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ButtonsLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.VisualizeTab)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.ButtonsLayout.addWidget(self.label_3)
        self.horizontalLayout_7.addLayout(self.ButtonsLayout)
        self.ButtonsLayout_2 = QtWidgets.QVBoxLayout()
        self.ButtonsLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.ButtonsLayout_2.setContentsMargins(25, 25, 25, 0)
        self.ButtonsLayout_2.setSpacing(5)
        self.ButtonsLayout_2.setObjectName("ButtonsLayout_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.VisualizeTab)
        self.graphicsView_2.setEnabled(False)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.ButtonsLayout_2.addWidget(self.graphicsView_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.PlayButton = QtWidgets.QPushButton(self.VisualizeTab)
        self.PlayButton.setObjectName("PlayButton")
        self.horizontalLayout_4.addWidget(self.PlayButton)
        self.PauseButton = QtWidgets.QPushButton(self.VisualizeTab)
        self.PauseButton.setObjectName("PauseButton")
        self.horizontalLayout_4.addWidget(self.PauseButton)
        self.RewindButton = QtWidgets.QPushButton(self.VisualizeTab)
        self.RewindButton.setObjectName("RewindButton")
        self.horizontalLayout_4.addWidget(self.RewindButton)
        self.ButtonsLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7.addLayout(self.ButtonsLayout_2)
        self.line_3 = QtWidgets.QFrame(self.VisualizeTab)
        self.line_3.setStyleSheet("line-color: transparent;\n"
"")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_7.addWidget(self.line_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.TrialInfoLable = QtWidgets.QLabel(self.VisualizeTab)
        self.TrialInfoLable.setStyleSheet("font: -10 11pt \"Tahoma\";")
        self.TrialInfoLable.setObjectName("TrialInfoLable")
        self.verticalLayout_6.addWidget(self.TrialInfoLable, 0, QtCore.Qt.AlignHCenter)
        self.InfoTextBox = QtWidgets.QTextBrowser(self.VisualizeTab)
        self.InfoTextBox.setObjectName("InfoTextBox")
        self.verticalLayout_6.addWidget(self.InfoTextBox, 0, QtCore.Qt.AlignHCenter)
        self.SaveAsButton = QtWidgets.QPushButton(self.VisualizeTab)
        self.SaveAsButton.setStyleSheet("font: -10 11pt \"Tahoma\";\n"
"color: rgb(36, 86, 97);\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 2px;\n"
"    border-color: black;\n"
"background-color:rgb(244, 244, 244)")
        self.SaveAsButton.setObjectName("SaveAsButton")
        self.verticalLayout_6.addWidget(self.SaveAsButton)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.VisualizeTab, "")
        self.PredictTab = QtWidgets.QWidget()
        self.PredictTab.setObjectName("PredictTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.PredictTab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LableLayout = QtWidgets.QVBoxLayout()
        self.LableLayout.setObjectName("LableLayout")
        self.PredictionLable = QtWidgets.QLabel(self.PredictTab)
        self.PredictionLable.setStyleSheet("font: -10 11pt \"Tahoma\";\n"
"")
        self.PredictionLable.setObjectName("PredictionLable")
        self.LableLayout.addWidget(self.PredictionLable)
        self.listView = QtWidgets.QListView(self.PredictTab)
        self.listView.setObjectName("listView")
        self.LableLayout.addWidget(self.listView)
        self.horizontalLayout_2.addLayout(self.LableLayout)
        spacerItem1 = QtWidgets.QSpacerItem(200, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PredictButton = QtWidgets.QPushButton(self.PredictTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PredictButton.sizePolicy().hasHeightForWidth())
        self.PredictButton.setSizePolicy(sizePolicy)
        self.PredictButton.setMinimumSize(QtCore.QSize(300, 150))
        self.PredictButton.setStyleSheet("font: -35 20pt \"Segoe Print\";\n"
"border-style: outset;\n"
"    border-width: 3.5px;\n"
"    border-radius: 25px;\n"
"    border-color:rgb(51, 99, 111);\n"
"background-color:rgb(245, 244, 255)\n"
"")
        self.PredictButton.setObjectName("PredictButton")
        self.verticalLayout.addWidget(self.PredictButton)
        self.ResultLable = QtWidgets.QLabel(self.PredictTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultLable.sizePolicy().hasHeightForWidth())
        self.ResultLable.setSizePolicy(sizePolicy)
        self.ResultLable.setMinimumSize(QtCore.QSize(700, 300))
        self.ResultLable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ResultLable.setStyleSheet("color: rgb(189, 189, 189);\n"
"font: 24pt \"Tahoma\";")
        self.ResultLable.setTextFormat(QtCore.Qt.AutoText)
        self.ResultLable.setAlignment(QtCore.Qt.AlignCenter)
        self.ResultLable.setObjectName("ResultLable")
        self.verticalLayout.addWidget(self.ResultLable)
        self.ClassifierButton = QtWidgets.QPushButton(self.PredictTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClassifierButton.sizePolicy().hasHeightForWidth())
        self.ClassifierButton.setSizePolicy(sizePolicy)
        self.ClassifierButton.setMinimumSize(QtCore.QSize(450, 60))
        self.ClassifierButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ClassifierButton.setStyleSheet("font: -10 11pt \"Tahoma\";\n"
"color: rgb(36, 86, 97);\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 2px;\n"
"    border-color: black;\n"
"background-color:rgb(244, 244, 244)")
        self.ClassifierButton.setObjectName("ClassifierButton")
        self.verticalLayout.addWidget(self.ClassifierButton, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(200, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.PredictTab, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(40, -30, 211, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/סמל.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(-13, 0, 311, 81))
        self.label_8.setText("")
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.tabWidget.raise_()
        self.label_8.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TobeginText.setText(_translate("MainWindow", "To begin, set your database."))
        self.BrowseButton.setText(_translate("MainWindow", "Browse"))
        self.BlackBackground.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.StartTab), _translate("MainWindow", "Page"))
        self.Datalabel.setText(_translate("MainWindow", "Data Loaded"))
        self.ReloadButton.setText(_translate("MainWindow", "Reload..."))
        item = self.DataTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Example Trial"))
        item = self.DataTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "SubjectID"))
        item = self.DataTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "IsLeftHanded"))
        item = self.DataTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Behavioral Data"))
        __sortingEnabled = self.DataTable.isSortingEnabled()
        self.DataTable.setSortingEnabled(False)
        item = self.DataTable.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.DataTable.item(0, 1)
        item.setText(_translate("MainWindow", "Yes"))
        item = self.DataTable.item(0, 2)
        item.setText(_translate("MainWindow", "...."))
        self.DataTable.setSortingEnabled(__sortingEnabled)
        self.CurrentConfigurationLable.setText(_translate("MainWindow", "Current Configuration"))
        self.LoadButton.setText(_translate("MainWindow", "Load..."))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.ConfigurationTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">Enter your configuration here</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DataTab), _translate("MainWindow", "Data"))
        self.HeatmapButton.setText(_translate("MainWindow", "Heatmap"))
        self.SaccadeTraceButton.setText(_translate("MainWindow", "Saccade Trace"))
        self.PlayButton.setText(_translate("MainWindow", "Play"))
        self.PauseButton.setText(_translate("MainWindow", "Pause"))
        self.RewindButton.setText(_translate("MainWindow", "Rewind"))
        self.TrialInfoLable.setText(_translate("MainWindow", "Trial Info"))
        self.InfoTextBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">Should we show this for single trial? </span><span style=\" font-size:8.25pt; font-weight:600;\">Yes</span></p></body></html>"))
        self.SaveAsButton.setText(_translate("MainWindow", "Save as..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VisualizeTab), _translate("MainWindow", "Visualize"))
        self.PredictionLable.setText(_translate("MainWindow", "Prediction Label:"))
        self.PredictButton.setText(_translate("MainWindow", "Predict"))
        self.ResultLable.setText(_translate("MainWindow", "Result..."))
        self.ClassifierButton.setText(_translate("MainWindow", "Change classifier Properties"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PredictTab), _translate("MainWindow", "Predict"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def Browse_Button_clicked(self):
        #path = QtWidgets.QFileDialog.getExistingDirectory(self, 'open directory', '', '')
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.gif)")
        print("BROWSE CLICKED!")

import temp_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

