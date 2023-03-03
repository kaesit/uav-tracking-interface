import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


#?PySide6
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QGuiApplication
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtQml import QQmlApplicationEngine

from requests import cookies

from themes.ui_splash_screen import Ui_SplashScreen

from themes.ui_main_window import Ui_MainWindow

from themes.circular_progress import CircularProgress

from ai import AI

import pymysql

import webbrowser  


cnx = pymysql.connect(user='root', password='esadphpmyadmin', host='localhost', database='blogdb')

cursor = cnx.cursor()

counter = 0

kontrol = True

class Main_Window(QMainWindow):
     def __init__(self):
          QMainWindow.__init__(self)
          self.ui = Ui_MainWindow()
          self.ui.setupUi(self)
          self.ui.centralwidget.setMinimumSize(800, 572)
          self.setWindowFlag(Qt.FramelessWindowHint)
          self.setAttribute(Qt.WA_TranslucentBackground)
          self.shadow = QGraphicsDropShadowEffect(self)
          self.shadow.setBlurRadius(20)
          self.shadow.setXOffset(0)
          self.shadow.setYOffset(0)
          self.shadow.setColor(QColor(0, 0, 0, 60))
          self.ui.bg.setGraphicsEffect(self.shadow)

          self.center()


          self.ui.btnMissile.clicked.connect(self.connect_to_ai)
          self.ui.btnLogout.clicked.connect(self.close_all_windows)
          self.ui.btnLink.clicked.connect(self.contact_us)

     def connect_to_ai(self):
          AI()
     def close_all_windows(self):
          sys.exit(0)
     def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
     def contact_us(self):
          url = "https://github.com/kaesit"
          webbrowser.open(url, new=0, autoraise=True)
          
class SplashScreen(QMainWindow):
     def __init__(self):
          QMainWindow.__init__(self)
          self.ui = Ui_SplashScreen()
          self.ui.setupUi(self)

          self.setWindowFlag(Qt.FramelessWindowHint)
          self.setAttribute(Qt.WA_TranslucentBackground)
          self.shadow = QGraphicsDropShadowEffect(self)
          self.shadow.setBlurRadius(20)
          self.shadow.setXOffset(0)
          self.shadow.setYOffset(0)
          self.shadow.setColor(QColor(0, 0, 0, 60))
          self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

          ## QTIMER ==> START
          self.timer = QtCore.QTimer()
          self.timer.timeout.connect(self.progress)
          # TIMER IN MILLISECONDS
          self.timer.start(35)

          # CHANGE DESCRIPTION

          # Initial Text
          self.ui.label_description.setText("<strong>PROGRAMIMA</strong> HOŞ GELDİNİZ")

          # Change Texts
          QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>ARAYÜZ</strong> Yükleniyor"))
          QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>Yapay Zeka</strong> Yükleniyor"))
          self.show()
     def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()
            self.close()
            # SHOW MAIN WINDOW
            self.main = Main_Window()
            self.main.show()

            # CLOSE SPLASH SCREEN
            

        # INCREASE COUNTER
        counter += 1

class LoginWindow:
     def __init__(self):
          self.window = QWidget()
          self.window.setFixedSize(330, 160)
          self.window.setWindowTitle("Missile Tracking Verify Form")
          self.window.setStyleSheet("""
               QWidget{
                    background-color:#191919;
               }
          """)

          self.window.setWindowIcon(QIcon("WolfCoder.ico"))

          self.userbox = QLineEdit()
          self.passbox = QLineEdit()
          self.mailbox = QLineEdit()
          
          self.userbox.setPlaceholderText("Username")
          self.passbox.setPlaceholderText("Password")
          self.mailbox.setPlaceholderText("EMail")

          self.userbox.setStyleSheet(open("qss/lineEdit.qss", "r").read())
          self.passbox.setStyleSheet(open("qss/lineEdit.qss", "r").read())
          self.mailbox.setStyleSheet(open("qss/lineEdit.qss", "r").read())

          self.passbox.setEchoMode(QLineEdit.Password)

          self.btn = QPushButton("Login")

          self.btn.setStyleSheet(open("qss/custombutton.qss", "r").read())

          self.btnregister = QPushButton("Register")

          self.btnregister.setStyleSheet(open("qss/custombutton.qss", "r").read())





          self.userlabel = QLabel("Username: ")
          self.userlabel.setObjectName("userlbl")
          self.passlabel = QLabel("Password:")
          self.passlabel.setObjectName("passlbl")
          self.maillabel = QLabel("EMail: ")


          self.btn.clicked.connect(self.check_password)

          self.btnregister.clicked.connect(self.new_account)

          self.keeplogin = QCheckBox("Keep me login")


          self.layout = QGridLayout()

          #self.layout.addWidget(self.userlabel, 0, 0)
          self.layout.addWidget(self.userbox, 0, 1)
          #self.layout.addWidget(self.passlabel, 1, 0)
          self.layout.addWidget(self.passbox, 1, 1)
          #self.layout.addWidget(self.maillabel, 2, 0)
          self.layout.addWidget(self.mailbox, 2, 1)
          self.layout.addWidget(self.btn, 3, 0, 1, 3)
          self.layout.addWidget(self.btnregister, 4, 0, 2, 3)


          self.window.setLayout(self.layout)

          self.window.show()
     def check_password(self):
          userel = self.userbox.text()
          passel = self.passbox.text()
          mailel = self.mailbox.text()
          cnx = pymysql.connect(user='{youruser}', password='{yourpassword}', host='{yourhost}', database='{yourdatabase}')
          imlec = cnx.cursor()
          find_user = ("SELECT * FROM eusers WHERE username = %s AND password = %s AND mail = %s")
          imlec.execute(find_user, [(self.userbox.text()), (self.passbox.text()), (self.mailbox.text())])
          result = imlec.fetchall()
          msg = QMessageBox()
          msg.setWindowTitle("System")
          msg.setStyleSheet(u"QLabel{min-width:120 px; font-size: 12px;} QPushButton{ width:60px; font-size: 9px; }");
          if self.userbox.text() == "" or self.passbox.text() == "" or self.mailbox.text() == "":
               msg.setText("Error")
               msg.setIcon(QMessageBox.Warning)
               msg.addButton("Okey", QMessageBox.YesRole)
               msg.setIcon(QMessageBox.Critical)
               msg.exec_()
          else:
               if result:
                    msg.setText('Success')
                    msg.setIcon(QMessageBox.Information)
                    msg.addButton("Okey", QMessageBox.YesRole)
                    msg.exec_()
                    
                    self.window.close()
                    self.mn = SplashScreen()
                    self.mn.show()
               else:
                    msg.setText('Incorrect Password')
                    msg.addButton("Okey", QMessageBox.YesRole)
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
     def new_account(self):
          msg2 = QMessageBox()
          
          cursor2 = cnx.cursor()
          if self.userbox.text() == "" or self.passbox.text() == "" or self.mailbox.text() == "":
               msg3 = QMessageBox()
               msg3.setText("Error")
               msg3.setIcon(QMessageBox.Warning)
               msg3.addButton("Okey", QMessageBox.YesRole)
               msg3.exec_()
          else:
               cursor2.execute("SELECT * FROM eusers WHERE EUEMail = %s", self.mailbox.text())
               row = cursor2.fetchone()
               cnx = pymysql.connect(user='{youruser}', password='{yourpassword}', host='{yourhost}', database='{yourdatabase}')
               if row!= None:
                    msg2.setText("This email already exists")
                    msg2.setIcon(QMessageBox.Warning)
                    msg2.addButton("Okey", QMessageBox.YesRole)
                    msg2.exec_()
               else:
                    cursor2.execute("INSERT INTO users VALUES(%s, %s, %s)", (self.userbox.text(),self.passbox.text(),self.mailbox.text()))

                    cnx.commit()
                    cnx.close()

                    msg2.setText("Register Successfully")
                    msg2.setIcon(QMessageBox.Information)
                    msg2.addButton("Okey", QMessageBox.YesRole)
                    msg2.exec_()

if __name__ =='__main__':
     app = QApplication(sys.argv)
     window = LoginWindow()
     app.exec_()



