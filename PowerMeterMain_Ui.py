# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Nov 17 21:33:31 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 272)
        MainWindow.setStyleSheet("background-color: #2980B9;\n"
"")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setCursor(QtCore.Qt.BlankCursor)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setStyleSheet("QTabWidget{background-color:#2980B9;\n"
"border: none;}\n"
"QTabBar::tab { background:#0D4E78;\n"
"border: none; \n"
"padding: 8px;\n"
"font-size: 11pt;\n"
"font-family: Lato;}\n"
"QTabBar::tab:selected{\n"
"color: #FFA22C;\n"
"font: bold;}\n"
"QTabBar::tab:!selected{\n"
"color: #7EB7DC;}\n"
"QTabWidget::tab-bar {\n"
"alignment: center;}\n"
"")
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(10, 0, 441, 71))
        self.frame.setStyleSheet("QLabel { background-color : none; color : #7EB7DC; font: bold 20pt;}\n"
"QFrame{background-color:#0D4E78;}")
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 31, 31))
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setMidLineWidth(0)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(180, 10, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setMidLineWidth(0)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(310, 10, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setMidLineWidth(0)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(140, 10, 21, 51))
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtGui.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(290, 10, 21, 51))
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.frame_2 = QtGui.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(10, 90, 441, 111))
        self.frame_2.setStyleSheet("QFrame{background-color:#0D4E78;}\n"
"Line{color:#7EB7DC; }")
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.lcdPowerPhase2 = QtGui.QLCDNumber(self.frame_2)
        self.lcdPowerPhase2.setGeometry(QtCore.QRect(180, 30, 101, 51))
        self.lcdPowerPhase2.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdPowerPhase2.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdPowerPhase2.setSmallDecimalPoint(False)
        self.lcdPowerPhase2.setNumDigits(5)
        self.lcdPowerPhase2.setDigitCount(5)
        self.lcdPowerPhase2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdPowerPhase2.setProperty("value", 0.0)
        self.lcdPowerPhase2.setObjectName("lcdPowerPhase2")
        self.lcdPowerPhase3 = QtGui.QLCDNumber(self.frame_2)
        self.lcdPowerPhase3.setGeometry(QtCore.QRect(320, 30, 101, 51))
        self.lcdPowerPhase3.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdPowerPhase3.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdPowerPhase3.setSmallDecimalPoint(False)
        self.lcdPowerPhase3.setNumDigits(5)
        self.lcdPowerPhase3.setDigitCount(5)
        self.lcdPowerPhase3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdPowerPhase3.setProperty("value", 0.0)
        self.lcdPowerPhase3.setObjectName("lcdPowerPhase3")
        self.lcdPowerPhase1 = QtGui.QLCDNumber(self.frame_2)
        self.lcdPowerPhase1.setGeometry(QtCore.QRect(30, 30, 101, 51))
        self.lcdPowerPhase1.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdPowerPhase1.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdPowerPhase1.setSmallDecimalPoint(False)
        self.lcdPowerPhase1.setNumDigits(5)
        self.lcdPowerPhase1.setDigitCount(5)
        self.lcdPowerPhase1.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdPowerPhase1.setProperty("value", 0.0)
        self.lcdPowerPhase1.setObjectName("lcdPowerPhase1")
        self.line = QtGui.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(150, 30, 3, 61))
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_4 = QtGui.QFrame(self.frame_2)
        self.line_4.setGeometry(QtCore.QRect(300, 30, 3, 61))
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/House-32.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/Images/House-32_or.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame_3 = QtGui.QFrame(self.tab_3)
        self.frame_3.setGeometry(QtCore.QRect(130, 0, 321, 51))
        self.frame_3.setStyleSheet("QLabel { background-color : none; color : #7EB7DC; font: bold 18pt;qproperty-alignment: \'AlignHCenter | AlignVCenter\';}\n"
"QFrame{background-color:#0D4E78;}")
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.label_12 = QtGui.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setMidLineWidth(0)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtGui.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(110, 0, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setMidLineWidth(0)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtGui.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(220, 0, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setMidLineWidth(0)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.line_5 = QtGui.QFrame(self.frame_3)
        self.line_5.setGeometry(QtCore.QRect(90, 10, 21, 31))
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtGui.QFrame(self.frame_3)
        self.line_6.setGeometry(QtCore.QRect(200, 10, 21, 31))
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label = QtGui.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.label.setStyleSheet("QLabel { background-color :#0D4E78; color : #7EB7DC; font: bold 14pt;padding: 2px}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 51, 51))
        self.label_11.setStyleSheet("QLabel { background-color :#0D4E78; }")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_2 = QtGui.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.label_2.setStyleSheet("QLabel { background-color :#0D4E78; color : #7EB7DC; font: bold 14pt;padding: 2px}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtGui.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(10, 140, 101, 31))
        self.label_7.setStyleSheet("QLabel { background-color :#0D4E78; color : #7EB7DC; font: bold 14pt;padding: 2px}")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(10, 180, 101, 31))
        self.label_8.setStyleSheet("QLabel { background-color :#0D4E78; color : #7EB7DC; font: bold 14pt;padding: 2px}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(60, 0, 51, 51))
        self.label_9.setStyleSheet("QLabel { background-color :#0D4E78; }")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.line_7 = QtGui.QFrame(self.tab_3)
        self.line_7.setGeometry(QtCore.QRect(50, 10, 21, 31))
        self.line_7.setStyleSheet("background-color:#0D4E78;")
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.frame_4 = QtGui.QFrame(self.tab_3)
        self.frame_4.setGeometry(QtCore.QRect(130, 60, 321, 31))
        self.frame_4.setStyleSheet("QFrame{background-color:#0D4E78;}")
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_4.setLineWidth(1)
        self.frame_4.setMidLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.line_12 = QtGui.QFrame(self.frame_4)
        self.line_12.setGeometry(QtCore.QRect(90, 5, 21, 21))
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setFrameShape(QtGui.QFrame.VLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.lcdVoltagePhase1 = QtGui.QLCDNumber(self.frame_4)
        self.lcdVoltagePhase1.setGeometry(QtCore.QRect(20, 0, 61, 31))
        self.lcdVoltagePhase1.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdVoltagePhase1.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdVoltagePhase1.setSmallDecimalPoint(False)
        self.lcdVoltagePhase1.setNumDigits(5)
        self.lcdVoltagePhase1.setDigitCount(5)
        self.lcdVoltagePhase1.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdVoltagePhase1.setProperty("value", 0.0)
        self.lcdVoltagePhase1.setObjectName("lcdVoltagePhase1")
        self.lcdVoltagePhase2 = QtGui.QLCDNumber(self.frame_4)
        self.lcdVoltagePhase2.setGeometry(QtCore.QRect(130, 0, 61, 31))
        self.lcdVoltagePhase2.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdVoltagePhase2.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdVoltagePhase2.setSmallDecimalPoint(False)
        self.lcdVoltagePhase2.setNumDigits(5)
        self.lcdVoltagePhase2.setDigitCount(5)
        self.lcdVoltagePhase2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdVoltagePhase2.setProperty("value", 0.0)
        self.lcdVoltagePhase2.setObjectName("lcdVoltagePhase2")
        self.lcdVoltagePhase3 = QtGui.QLCDNumber(self.frame_4)
        self.lcdVoltagePhase3.setGeometry(QtCore.QRect(230, 0, 61, 31))
        self.lcdVoltagePhase3.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdVoltagePhase3.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdVoltagePhase3.setSmallDecimalPoint(False)
        self.lcdVoltagePhase3.setNumDigits(5)
        self.lcdVoltagePhase3.setDigitCount(5)
        self.lcdVoltagePhase3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdVoltagePhase3.setProperty("value", 0.0)
        self.lcdVoltagePhase3.setObjectName("lcdVoltagePhase3")
        self.line_13 = QtGui.QFrame(self.frame_4)
        self.line_13.setGeometry(QtCore.QRect(200, 5, 21, 21))
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setFrameShape(QtGui.QFrame.VLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.frame_5 = QtGui.QFrame(self.tab_3)
        self.frame_5.setGeometry(QtCore.QRect(130, 100, 321, 31))
        self.frame_5.setStyleSheet("QFrame{background-color:#0D4E78;}")
        self.frame_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_5.setLineWidth(1)
        self.frame_5.setMidLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.line_14 = QtGui.QFrame(self.frame_5)
        self.line_14.setGeometry(QtCore.QRect(90, 5, 21, 21))
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setFrameShape(QtGui.QFrame.VLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.lcdCurrentPhase1 = QtGui.QLCDNumber(self.frame_5)
        self.lcdCurrentPhase1.setGeometry(QtCore.QRect(20, 0, 61, 31))
        self.lcdCurrentPhase1.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdCurrentPhase1.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdCurrentPhase1.setSmallDecimalPoint(False)
        self.lcdCurrentPhase1.setNumDigits(5)
        self.lcdCurrentPhase1.setDigitCount(5)
        self.lcdCurrentPhase1.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdCurrentPhase1.setProperty("value", 0.0)
        self.lcdCurrentPhase1.setObjectName("lcdCurrentPhase1")
        self.lcdCurrentPhase2 = QtGui.QLCDNumber(self.frame_5)
        self.lcdCurrentPhase2.setGeometry(QtCore.QRect(130, 0, 61, 31))
        self.lcdCurrentPhase2.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdCurrentPhase2.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdCurrentPhase2.setSmallDecimalPoint(False)
        self.lcdCurrentPhase2.setNumDigits(5)
        self.lcdCurrentPhase2.setDigitCount(5)
        self.lcdCurrentPhase2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdCurrentPhase2.setProperty("value", 0.0)
        self.lcdCurrentPhase2.setObjectName("lcdCurrentPhase2")
        self.lcdCurrentPhase3 = QtGui.QLCDNumber(self.frame_5)
        self.lcdCurrentPhase3.setGeometry(QtCore.QRect(230, 0, 61, 31))
        self.lcdCurrentPhase3.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdCurrentPhase3.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdCurrentPhase3.setSmallDecimalPoint(False)
        self.lcdCurrentPhase3.setNumDigits(5)
        self.lcdCurrentPhase3.setDigitCount(5)
        self.lcdCurrentPhase3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdCurrentPhase3.setProperty("value", 0.0)
        self.lcdCurrentPhase3.setObjectName("lcdCurrentPhase3")
        self.line_15 = QtGui.QFrame(self.frame_5)
        self.line_15.setGeometry(QtCore.QRect(200, 5, 21, 21))
        self.line_15.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_15.setFrameShape(QtGui.QFrame.VLine)
        self.line_15.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.frame_6 = QtGui.QFrame(self.tab_3)
        self.frame_6.setGeometry(QtCore.QRect(130, 140, 321, 31))
        self.frame_6.setStyleSheet("QFrame{background-color:#0D4E78;}")
        self.frame_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_6.setLineWidth(1)
        self.frame_6.setMidLineWidth(0)
        self.frame_6.setObjectName("frame_6")
        self.line_16 = QtGui.QFrame(self.frame_6)
        self.line_16.setGeometry(QtCore.QRect(90, 5, 21, 21))
        self.line_16.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_16.setFrameShape(QtGui.QFrame.VLine)
        self.line_16.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.lcdPowerPhase12 = QtGui.QLCDNumber(self.frame_6)
        self.lcdPowerPhase12.setGeometry(QtCore.QRect(20, 0, 61, 31))
        self.lcdPowerPhase12.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdPowerPhase12.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdPowerPhase12.setSmallDecimalPoint(False)
        self.lcdPowerPhase12.setNumDigits(5)
        self.lcdPowerPhase12.setDigitCount(5)
        self.lcdPowerPhase12.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdPowerPhase12.setProperty("value", 0.0)
        self.lcdPowerPhase12.setObjectName("lcdPowerPhase12")
        self.lcdPowerPhase22 = QtGui.QLCDNumber(self.frame_6)
        self.lcdPowerPhase22.setGeometry(QtCore.QRect(130, 0, 61, 31))
        self.lcdPowerPhase22.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdPowerPhase22.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdPowerPhase22.setSmallDecimalPoint(False)
        self.lcdPowerPhase22.setNumDigits(5)
        self.lcdPowerPhase22.setDigitCount(5)
        self.lcdPowerPhase22.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdPowerPhase22.setProperty("value", 0.0)
        self.lcdPowerPhase22.setObjectName("lcdPowerPhase22")
        self.lcdPowerPhase33 = QtGui.QLCDNumber(self.frame_6)
        self.lcdPowerPhase33.setGeometry(QtCore.QRect(230, 0, 61, 31))
        self.lcdPowerPhase33.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdPowerPhase33.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdPowerPhase33.setSmallDecimalPoint(False)
        self.lcdPowerPhase33.setNumDigits(5)
        self.lcdPowerPhase33.setDigitCount(5)
        self.lcdPowerPhase33.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdPowerPhase33.setProperty("value", 0.0)
        self.lcdPowerPhase33.setObjectName("lcdPowerPhase33")
        self.line_17 = QtGui.QFrame(self.frame_6)
        self.line_17.setGeometry(QtCore.QRect(200, 5, 21, 21))
        self.line_17.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_17.setFrameShape(QtGui.QFrame.VLine)
        self.line_17.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.frame_7 = QtGui.QFrame(self.tab_3)
        self.frame_7.setGeometry(QtCore.QRect(130, 180, 321, 31))
        self.frame_7.setStyleSheet("QFrame{background-color:#0D4E78;}")
        self.frame_7.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_7.setLineWidth(1)
        self.frame_7.setMidLineWidth(0)
        self.frame_7.setObjectName("frame_7")
        self.line_18 = QtGui.QFrame(self.frame_7)
        self.line_18.setGeometry(QtCore.QRect(90, 5, 21, 21))
        self.line_18.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_18.setFrameShape(QtGui.QFrame.VLine)
        self.line_18.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.lcdPowerFactorPhase1 = QtGui.QLCDNumber(self.frame_7)
        self.lcdPowerFactorPhase1.setGeometry(QtCore.QRect(20, 0, 61, 31))
        self.lcdPowerFactorPhase1.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdPowerFactorPhase1.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdPowerFactorPhase1.setSmallDecimalPoint(False)
        self.lcdPowerFactorPhase1.setNumDigits(5)
        self.lcdPowerFactorPhase1.setDigitCount(5)
        self.lcdPowerFactorPhase1.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdPowerFactorPhase1.setProperty("value", 0.0)
        self.lcdPowerFactorPhase1.setObjectName("lcdPowerFactorPhase1")
        self.lcdPowerFactorPhase2 = QtGui.QLCDNumber(self.frame_7)
        self.lcdPowerFactorPhase2.setGeometry(QtCore.QRect(130, 0, 61, 31))
        self.lcdPowerFactorPhase2.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdPowerFactorPhase2.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdPowerFactorPhase2.setSmallDecimalPoint(False)
        self.lcdPowerFactorPhase2.setNumDigits(5)
        self.lcdPowerFactorPhase2.setDigitCount(5)
        self.lcdPowerFactorPhase2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdPowerFactorPhase2.setProperty("value", 0.0)
        self.lcdPowerFactorPhase2.setObjectName("lcdPowerFactorPhase2")
        self.lcdPowerFactorPhase3 = QtGui.QLCDNumber(self.frame_7)
        self.lcdPowerFactorPhase3.setGeometry(QtCore.QRect(230, 0, 61, 31))
        self.lcdPowerFactorPhase3.setStyleSheet("QLCDNumber{color: white;}")
        self.lcdPowerFactorPhase3.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdPowerFactorPhase3.setSmallDecimalPoint(False)
        self.lcdPowerFactorPhase3.setNumDigits(5)
        self.lcdPowerFactorPhase3.setDigitCount(5)
        self.lcdPowerFactorPhase3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdPowerFactorPhase3.setProperty("value", 0.0)
        self.lcdPowerFactorPhase3.setObjectName("lcdPowerFactorPhase3")
        self.line_19 = QtGui.QFrame(self.frame_7)
        self.line_19.setGeometry(QtCore.QRect(200, 5, 21, 21))
        self.line_19.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_19.setFrameShape(QtGui.QFrame.VLine)
        self.line_19.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/Power-32_bk.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/Images/Power-32_or.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_3, icon1, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(70, 0, 51, 51))
        self.label_10.setStyleSheet("QLabel { background-color :#0D4E78; }")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_21 = QtGui.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(120, 0, 131, 51))
        self.label_21.setStyleSheet("QLabel { background-color :#0D4E78; color : #7EB7DC; font: bold 14pt;}")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtGui.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(320, 0, 131, 51))
        self.label_22.setStyleSheet("QLabel { background-color :#0D4E78; color : #7EB7DC; font: bold 14pt;}")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtGui.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(270, 0, 51, 51))
        self.label_23.setStyleSheet("QLabel { background-color :#0D4E78; }")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Images/Humidity-32.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/Images/Humidity-32_or.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Medidor de Energia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/Images/Plug-02-32.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Fase 1</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Fase 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Fase 3", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Principal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Fase 1</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Fase 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Fase 3", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Voltaje", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/Images/Shape-Lightning-32.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Corriente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Potencia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "FP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/Images/Plug-02-32.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Variables Electricas", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/Images/Instrument-Thermometer-32.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "Temperatura", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "Humedad", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/Images/Humidity-32.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Temp/Humedad", None, QtGui.QApplication.UnicodeUTF8))

import PowerMeterResource
