from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtGui import QIntValidator
from sistema.Sistema import ControlloreSistema
from utilizzatore.model.Dipendente import Dipendente


class VistaInserisciDipendente(QWidget):

    def __init__(self, controller, callback, parent=None):
        super(VistaInserisciDipendente, self).__init__(parent)
        uic.loadUi('utilizzatore/view/vista_inserisci_staff.ui', self)
        self.controller = controller
        self.callback = callback
        self.textTelefono.setValidator(QIntValidator())
        self.controllerSistema = ControlloreSistema()
        self.btn_ok.clicked.connect(self.add_dipendente)

    def add_dipendente(self):
        nome = self.textNome.text()
        cognome = self.textCognome.text()
        cf = self.textCodiceFiscale.text()
        indirizzo = self.textIndirizzo.text()
        email = self.textEmail.text()
        telefono = self.textTelefono.text()
        boolCF = self.controllerSistema.controlloCF(cf)
        if nome == "" or cognome == "" or cf == "" or indirizzo == "" or email == "" or telefono == "" or boolCF == False:
            msg = QMessageBox(
                text="Errore!",
                parent=None)
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setInformativeText("")
            msg.setWindowTitle("Errore!")
            msg.exec()
        else:
            self.controller.aggiungi_dipendente(Dipendente(
                nome,
                cognome,
                cf,
                indirizzo,
                email,
                telefono)
            )
            self.callback()
            self.close()