from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtGui import QIntValidator

from obj.Abbonamenti import Abbonamenti


class VistaInserisciAbbonamenti(QWidget):

    def __init__(self, controller, callback, parent=None):
        super(VistaInserisciAbbonamenti, self).__init__(parent)
        uic.loadUi('utilizzatore/view/vista_inserisci_abbonamenti.ui', self)
        self.controller = controller
        self.callback = callback
        self.textPrezzo.setValidator(QIntValidator())
        self.textScadenza.setValidator(QIntValidator())
        self.comboBox.addItems(["Giornaliero","Mensile", "Semestrale", "Annuale", "Special"])
        self.btn_ok.clicked.connect(self.add_abbonamenti)

    def add_abbonamenti(self):
        tipo = self.comboBox.currentText()
        costo = self.textPrezzo.text()
        codice = "_" + str(self.controller.id_chooser())
        durata = self.textScadenza.text()
        if codice == "" or tipo == "" or costo == "" or durata == "":
            msg = QMessageBox(
                text="Errore!",
                parent=None)
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setInformativeText("")
            msg.setWindowTitle("Errore!")
            msg.exec()
        else:
            self.controller.aggiungi_abbonamenti(Abbonamenti(
                (tipo+codice).lower(),
                tipo,
                costo,
                durata)
            )
            self.callback()
            self.close()