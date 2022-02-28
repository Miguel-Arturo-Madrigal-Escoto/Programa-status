# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textoNota = QTextEdit(self.centralwidget)
        self.textoNota.setObjectName(u"textoNota")
        self.textoNota.setStyleSheet(u"border: none;")

        self.gridLayout.addWidget(self.textoNota, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.lineFecha = QLineEdit(self.centralwidget)
        self.lineFecha.setObjectName(u"lineFecha")
        self.lineFecha.setMaximumSize(QSize(400, 16777215))
        self.lineFecha.setStyleSheet(u"border: none;")

        self.horizontalLayout_3.addWidget(self.lineFecha)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineTitulo = QLineEdit(self.centralwidget)
        self.lineTitulo.setObjectName(u"lineTitulo")
        self.lineTitulo.setMaximumSize(QSize(400, 16777215))
        self.lineTitulo.setStyleSheet(u"border: none;")

        self.horizontalLayout_2.addWidget(self.lineTitulo)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.labelRuta = QLabel(self.centralwidget)
        self.labelRuta.setObjectName(u"labelRuta")
        self.labelRuta.setMinimumSize(QSize(400, 0))
        self.labelRuta.setMaximumSize(QSize(400, 16777215))
        self.labelRuta.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.labelRuta)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.labelNotepad = QLabel(self.centralwidget)
        self.labelNotepad.setObjectName(u"labelNotepad")
        self.labelNotepad.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"font-size: 16px;")

        self.gridLayout.addWidget(self.labelNotepad, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuAbrir = QMenu(self.menubar)
        self.menuAbrir.setObjectName(u"menuAbrir")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbrir.menuAction())
        self.menuAbrir.addAction(self.actionAbrir)
        self.menuAbrir.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_7.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_8.setText("")
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.label_5.setText("")
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ruta", None))
        self.labelRuta.setText("")
        self.label_11.setText("")
        self.labelNotepad.setText(QCoreApplication.translate("MainWindow", u"Notepad", None))
        self.menuAbrir.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

