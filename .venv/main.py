import io
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication
import random
from PyQt6.QtGui import QPainter, QColor, QPolygon

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>417</width>
    <height>398</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>300</y>
      <width>151</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>ОК</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>417</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setWindowTitle('Жёлтые круги')
        self.flag = False
        self.pushButton.clicked.connect(self.draw)
        self.coords = []

    def draw(self):
        self.size = random.randint(10, 100)
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))
            qp.setBrush(QColor(255, 255, 0))
            self.x, self.y = random.randint(1, 417), random.randint(0, 398)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
