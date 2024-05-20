import sys
from PyQt6.QtWidgets import QApplication
from home.VistaLogin import VistaLogin

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vistalogin = VistaLogin()
    vistalogin.show()
    sys.exit(app.exec())
