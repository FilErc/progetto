from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtGui import QIntValidator
from obj.Servizio import Servizio
class VistaInserisciServizio(QWidget):
    def __init__(self, controller, callback, parent=None):
        super(VistaInserisciServizio, self).__init__(parent)
        uic.loadUi('utilizzatore/view/vista_inserisci_servizio.ui', self)
        self.controller = controller
        self.callback = callback
        self.comboBox.addItems(["Racchetta e Palline", "Pallone da basket","Pallone e Guanti da calcio"])
        self.btn_ok.clicked.connect(self.add_servizio)
    def add_servizio(self):
        tipo = self.comboBox.currentText()
        codice = "_"+str(self.controller.id_chooser())
        if tipo == "":
            msg = QMessageBox(
                text="Errore!",
                parent=None)
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setInformativeText("")
            msg.setWindowTitle("Errore!")
            msg.exec()
        else:
            self.controller.aggiungi_servizio(Servizio(
                (tipo+codice).lower(),
                tipo)
            )
            self.callback()
            self.close()