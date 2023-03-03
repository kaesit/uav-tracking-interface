from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class CircularProgress(QWidget):
     def __init__(self):
         QWidget.__init__(self)

         self.width = 270
         self.height = 270
         self.progress_width = 10
         self.progress_rounded_cap = True
         self.progress_color = 0x498BD1
         self.max_value = 100
         self.value = 50
         self.font_family = "Seoge UI"
         self.font_size = 12
         self.suffix = "%"
         self.text_color = 0x498BD1
         self.enable_text = True

         self.enable_bg = True
         self.bg_color = 0x44475a

         #? Yerleştirmesiz Boyut Ayarı
         self.resize(self.width, self.height)

     def drop_shadow(self, enable):
          if enable:
               self.shadow = QGraphicsDropShadowEffect(self)
               self.shadow.setBlurRadius(15)
               self.shadow.setXOffset(0)
               self.shadow.setYOffset(0)
               self.shadow.setColor(QColor(0, 0, 0, 80))
               self.setGraphicsEffect(self.shadow)
               
     def set_value(self, value):
          self.value = value
          self.repaint()

     def paintEvent(self, e):
          width = self.width - self.progress_width
          height = self.height - self.progress_width
          margin = self.progress_width / 2
          value = self.value * 360 / self.max_value


          paint = QPainter()
          paint.begin(self)
          paint.setRenderHint(QPainter.Antialiasing)
          paint.setFont(QFont(self.font_family, self.font_size))
              
          rect = QRect(0, 0, self.width, self.height)
          paint.setPen(Qt.NoPen)
          paint.drawRect(rect)


          pen = QPen()
          pen.setColor(QColor(self.text_color))     
          pen.setWidth(self.progress_width)

          if self.progress_rounded_cap:
               pen.setCapStyle(Qt.RoundCap)

          if self.enable_bg:
               pen.setColor(QColor(self.bg_color))
               paint.setPen(pen)
               paint.drawArc(margin, margin,  width, height, 0, 360 * 16)

          
          pen.setColor(QColor(self.progress_color))     
          paint.setPen(pen)
          paint.drawArc(margin, margin,  width, height, -90 * 16, -value * 16)

          if self.enable_text:                    
               pen.setColor(QColor(self.text_color))
               paint.setPen(pen)
               paint.drawRect(rect, f"{self.value}{self.suffix}")


          paint.end()
