# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 572)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bg = QFrame(self.centralwidget)
        self.bg.setObjectName(u"bg")
        self.bg.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(56, 58, 89);\n"
"	color:rgb(220, 220, 220);\n"
"}")
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 25, 10, 25)
        self.btnMissile = QPushButton(self.bg)
        self.btnMissile.setObjectName(u"btnMissile")
        self.btnMissile.setMinimumSize(QSize(120, 40))
        self.btnMissile.setMaximumSize(QSize(520, 60))
        self.btnMissile.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(254, 121, 199);;\n"
"	color:rgba(241,250,255,255);\n"
"	border-radius:10px;\n"
"	font-size:20px;\n"
"	font-family:sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:rgba(255,255,255,255);\n"
"	border-radius:15px;\n"
"	font-size:20px;\n"
"	font-family:sans-serif;\n"
"	cursor:pointer;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/icons8_shutdown_96px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMissile.setIcon(icon)
        self.btnMissile.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.btnMissile, 2, 0, 1, 1)

        self.frame = QFrame(self.bg)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(120, 120))
        self.frame.setMaximumSize(QSize(800, 120))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnLink = QPushButton(self.frame)
        self.btnLink.setObjectName(u"btnLink")
        self.btnLink.setMinimumSize(QSize(120, 120))
        self.btnLink.setMaximumSize(QSize(800, 120))
        self.btnLink.setStyleSheet(u"background-color:transparent;")
        icon1 = QIcon()
        icon1.addFile(u"icons/icons8-business-group-90.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLink.setIcon(icon1)
        self.btnLink.setIconSize(QSize(120, 120))

        self.verticalLayout_3.addWidget(self.btnLink)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.btnLogout = QPushButton(self.bg)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setMinimumSize(QSize(120, 40))
        self.btnLogout.setMaximumSize(QSize(500, 60))
        self.btnLogout.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(254, 121, 199);;\n"
"	color:rgba(241,250,255,255);\n"
"	border-radius:10px;\n"
"	font-size:20px;\n"
"	font-family:sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:rgba(255,255,255,255);\n"
"	border-radius:15px;\n"
"	font-size:20px;\n"
"	font-family:sans-serif;\n"
"	cursor:pointer;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"icons/icons8_close_pane_96px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLogout.setIcon(icon2)
        self.btnLogout.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.btnLogout, 3, 0, 1, 1)

        self.label = QLabel(self.bg)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 55))
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setStyleSheet(u"font-size:45px;\n"
"color:rgb(254, 121, 199);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.bg)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnMissile.setText(QCoreApplication.translate("MainWindow", u"Activate Missile Tracking System", None))
        self.btnLink.setText("")
        self.btnLogout.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Missile Tracking", None))
    # retranslateUi

