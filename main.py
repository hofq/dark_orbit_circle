from PyQt5.QtCore    import Qt, QSize, QTimer
from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QWidget,
                            QPushButton, QGridLayout, QSpacerItem,
                            QSizePolicy, QLabel, QApplication)
import getpass



user = getpass.getuser()
path = "C:\\Users\\" + user + "\\Documents\\"


with open(path + 'test.txt') as f:
    Test = int(f.read())
    Test2 = Test/2-20

class Dialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setObjectName('dark_orbit_helper')
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet(Stylesheet % Test2)

        self.initUi()

    def initUi(self):
        # Important: this widget is used as background and rounded corners.
        self.widget = QWidget(self)
        self.widget.setObjectName('Custom_Widget')
        layout = QVBoxLayout(self)
        layout.addWidget(self.widget)

        # Add user interface to widget
        layout = QGridLayout(self.widget)
        layout.addItem(QSpacerItem(
            40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 0)
        layout.addWidget(QPushButton(
#            'r', self, clicked=self.accept, objectName='closeButton'), 0, 1, alignment=Qt.AlignCenter)
             'r', self, clicked=self.accept, objectName='closeButton'), 2, 0, 5, 2, alignment=Qt.AlignCenter)
#        layout.addWidget(QLabel("<h2 style='color:blue;'>Hello, world!</h2>"), 2, 0, 5, 2, alignment=Qt.AlignCenter)                           
    
    def sizeHint(self):
        return QSize(Test, Test)


Stylesheet = """
#Custom_Widget {

    border-radius: %s;
    opacity: 100;
    border: 2px solid #ff2025;
}
#closeButton {
    min-width: 36px;
    min-height: 36px;
    font-family: "Webdings";
    qproperty-text: "r";
    border-radius: 10px;
}
#closeButton:hover {
    color: #ccc;
    background: red;
}
"""


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Dialog()
    w.exec_()
    QTimer.singleShot(200, app.quit)
    sys.exit(app.exec_())