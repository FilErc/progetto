from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
from listadipendente.controller.controller_lista_dipendente import ControllerListaDipendente
from listaadmin.controller.controller_lista_admin import ControllerListaAdmin
class Registrazione(QWidget):
    def __init__(self, parent=None):
        super(Registrazione, self).__init__(parent)
        self.controller = ControllerListaClienti()
        self.controllerStaff = ControllerListaDipendente()
        self.controllerAdmin = ControllerListaAdmin()
        uic.loadUi("home/vistaregistrazione.ui", self)
        self.okBUT.clicked.connect(self.creation)
    def creation(self):
        CodiceFiscale = self.CodiceText.text()
        Username = self.UsernameText.text()
        Password = self.PasswordText.text()
        self.k = True
        f = open("listautenti/data/lista_utenti.txt", "r+")
        riga = f.readline()
        while riga != "":
            User = riga.split(":")
            if CodiceFiscale == User[0]:
                self.k = False
                break
            riga = f.readline()
        for cliente in  self.controller.get_lista_clienti():
            self.k = False
            if cliente.cf.lower() == CodiceFiscale.lower():
                self.k = True
                break
        for staff in self.controllerStaff.get_lista_dipendente():
            if staff.cf.lower() == CodiceFiscale.lower():
                self.k = True
                break
        for admin in self.controllerAdmin.get_lista_admin():
            if admin.cf.lower() == CodiceFiscale.lower():
                self.k = True
                break
        if self.k == True:
            f.write(CodiceFiscale + ":" + Username + ":" + Password + "\n")
        else:
            msg = QMessageBox(text="Il tuo codice fiscale è già collegato ad un altro account oppure hai lasciato dei campi nulli, riprova!", parent=None)
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setInformativeText("aga")
            msg.setWindowTitle("Errore!")
            msg.exec()
        f.close()
        self.close()