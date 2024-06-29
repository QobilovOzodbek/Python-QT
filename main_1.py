import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    win.setGeometry(950,300,500,500)
    win.setWindowTitle("Ozodbek Qobilov")
    win.setWindowIcon(QIcon("`icon.png`"))
    win.setToolTip("Ozodbek Qobilov")
    win.show()
    sys.exit(app.exec_())
    
window()
