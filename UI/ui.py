# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calcUI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, Signal)
from PySide2.QtGui import (QBrush, QColor, QCursor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class ClickLabel(QLabel):
    clicked = Signal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)

class Ui_window(object):
    def setupUi(self, window):
        if window.objectName():
            window.setObjectName(u"window")
        window.setWindowModality(Qt.NonModal)
        window.resize(410, 220)
        window.setMinimumSize(QSize(410, 220))
        window.setMaximumSize(QSize(410, 220))
        window.setFocusPolicy(Qt.NoFocus)
        window.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 391, 131))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.input_group_radio = QGroupBox(self.layoutWidget)
        self.input_group_radio.setObjectName(u"input_group_radio")
        self.input_group_radio.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout_6 = QVBoxLayout(self.input_group_radio)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.input_radio_1 = QRadioButton(self.input_group_radio)
        self.input_radio_1.setObjectName(u"input_radio_1")
        self.input_radio_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.input_radio_1.setChecked(True)

        self.verticalLayout_6.addWidget(self.input_radio_1)

        self.input_radio_2 = QRadioButton(self.input_group_radio)
        self.input_radio_2.setObjectName(u"input_radio_2")
        self.input_radio_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.input_radio_2)

        self.input_radio_3 = QRadioButton(self.input_group_radio)
        self.input_radio_3.setObjectName(u"input_radio_3")
        self.input_radio_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.input_radio_3)


        self.verticalLayout_2.addWidget(self.input_group_radio)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.input = QLineEdit(self.layoutWidget)
        self.input.setObjectName(u"input")

        self.verticalLayout_5.addWidget(self.input)

        self.output = QLineEdit(self.layoutWidget)
        self.output.setObjectName(u"output")
        self.output.setEnabled(True)
        self.output.setFrame(True)
        self.output.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.output)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.copy_link = ClickLabel(self.layoutWidget)
        self.copy_link.setObjectName(u"copy_link")
        self.copy_link.setCursor(QCursor(Qt.PointingHandCursor))
        self.copy_link.setFocusPolicy(Qt.NoFocus)
        self.copy_link.setStyleSheet(u"color: blue;")
        self.copy_link.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.copy_link)

        self.button = QPushButton(self.layoutWidget)
        self.button.setObjectName(u"button")
        self.button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.button)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.output_group_radio = QGroupBox(self.layoutWidget)
        self.output_group_radio.setObjectName(u"output_group_radio")
        self.verticalLayout_7 = QVBoxLayout(self.output_group_radio)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.output_radio_1 = QRadioButton(self.output_group_radio)
        self.output_radio_1.setObjectName(u"output_radio_1")
        self.output_radio_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.output_radio_1.setChecked(True)

        self.verticalLayout_7.addWidget(self.output_radio_1)

        self.output_radio_2 = QRadioButton(self.output_group_radio)
        self.output_radio_2.setObjectName(u"output_radio_2")
        self.output_radio_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.output_radio_2)

        self.output_radio_3 = QRadioButton(self.output_group_radio)
        self.output_radio_3.setObjectName(u"output_radio_3")
        self.output_radio_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.output_radio_3)


        self.verticalLayout.addWidget(self.output_group_radio)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 410, 26))
        window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(window)
        self.statusbar.setObjectName(u"statusbar")
        window.setStatusBar(self.statusbar)

        self.retranslateUi(window)

        QMetaObject.connectSlotsByName(window)
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"Calc", None))
        self.input_group_radio.setTitle(QCoreApplication.translate("window", u"\u0418\u0437", None))
        self.input_radio_1.setText(QCoreApplication.translate("window", u"2", None))
        self.input_radio_2.setText(QCoreApplication.translate("window", u"10", None))
        self.input_radio_3.setText(QCoreApplication.translate("window", u"16", None))
        self.label_3.setText(QCoreApplication.translate("window", u"\u0412\u0432\u043e\u0434", None))
        self.label_4.setText(QCoreApplication.translate("window", u"\u0412\u044b\u0432\u043e\u0434", None))
        self.output.setText("")
        self.copy_link.setText(QCoreApplication.translate("window", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.button.setText(QCoreApplication.translate("window", u"\u0421\u0447\u0438\u0442\u0430\u0442\u044c!", None))
        self.output_group_radio.setTitle(QCoreApplication.translate("window", u"\u0412", None))
        self.output_radio_1.setText(QCoreApplication.translate("window", u"2", None))
        self.output_radio_2.setText(QCoreApplication.translate("window", u"10", None))
        self.output_radio_3.setText(QCoreApplication.translate("window", u"16", None))
    # retranslateUi

