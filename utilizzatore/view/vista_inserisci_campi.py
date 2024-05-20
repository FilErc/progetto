from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtGui import QIntValidator

from obj.Campi import Campi


class VistaInserisciCampi(QWidget):

    def __init__(self, controller, callback, parent=None):
        super(VistaInserisciCampi, self).__init__(parent)
        uic.loadUi('utilizzatore/view/vista_inserisci_campi.ui', self)
        self.controller = controller
        self.callback = callback
        self.textDurata.setValidator(QIntValidator())
        self.comboBox.addItems(["Calcio a 5","Calcio a 8", "Basket", "Tennis", "Padel"])
        self.btn_ok.clicked.connect(self.add_campi)


    def add_campi(self):
        tipo = self.comboBox.currentText()
        codice = "_" + str(self.controller.id_chooser())
        durata = self.textDurata.text()
        if tipo == "" or codice == "" or durata == "":
            msg = QMessageBox(
                text="Errore!",
                parent=None)
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setInformativeText("")
            msg.setWindowTitle("Errore!")
            msg.exec()
        else:
            self.controller.aggiungi_campi(Campi(
                (tipo+codice).lower(),
                tipo,
                durata)
            )
            self.callback()
            self.close()