import io
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication
import random
from PyQt6.QtGui import QPainter, QColor, QPolygon
from UI import Ui_MainWindow
class Circles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Жёлтые круги')
        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.size = random.randint(10, 100)
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            qp.setPen(QColor(*colors))
            qp.setBrush(QColor(*colors))
            self.x, self.y = random.randint(1, 417), random.randint(0, 398)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    show = ex.show()
    sys.exit(app.exec())
