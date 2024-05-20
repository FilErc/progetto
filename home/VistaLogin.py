from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from home.VistaHome import VistaHome
from home.VistaRegistrazione import Registrazione
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
from listadipendente.controller.controller_lista_dipendente import ControllerListaDipendente
from listaadmin.controller.controller_lista_admin import ControllerListaAdmin
class VistaLogin(QWidget):
    k = False
    def __init__(self, parent=None):
        super(VistaLogin, self).__init__(parent)
        uic.loadUi('home/vistalogin.ui', self)
        self.loginBUT.clicked.connect(self.check_lista_utenti)
        self.registerBUT.clicked.connect(self.register)

    def check_cf_cliente(self, cf):
        self.controller = ControllerListaClienti()
        b = self.controller.get_cf_listacliente(cf)
        return b
    def check_cf_dipendente(self, cf):
        self.controller = ControllerListaDipendente()
        b = self.controller.get_cf_listadipendente(cf)
        return b
    def check_cf_admin(self,cf):
        self.controller = ControllerListaAdmin()
        b = self.controller.get_cf_listaadmin(cf)
        return b
    def check_lista_utenti(self):
        testo1 = self.UsernameText.text()
        testo2 = self.PasswordText.text()
        f = open("listautenti/data/lista_utenti.txt", "r")
        riga = f.readline()
        booleanBox = True
        while riga != "":
            User = riga.split(":")
            Password = User[2].translate(str.maketrans('', '', "\n"))
            Username = User[1]
            cf = User[0]
            booleanFiscalCodeCliente = self.check_cf_cliente(cf)
            booleanFiscalCodeDipendenti = self.check_cf_dipendente(cf)
            booleanFiscalCodeAdmin = self.check_cf_admin(cf)
            if testo1 == Username and testo2 == Password:
                if booleanFiscalCodeCliente or booleanFiscalCodeDipendenti or booleanFiscalCodeAdmin:
                    self.k = True
                    booleanBox = False
                    break

            riga = f.readline()
        if booleanBox:
            msg = QMessageBox(
                text="Il tuo codice fiscale è già collegato ad un altro account oppure hai lasciato dei campi nulli, riprova!",
                parent=None)
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setInformativeText("")
            msg.setWindowTitle("Errore!")
            msg.exec()
            self.PasswordText.clear()
            self.UsernameText.clear()
        f.close()
        if self.k == True:
            self.close()
            self.VistaHome = VistaHome(cf)
            self.VistaHome.show()
    def register(self):
        self.vista_registrazione = Registrazione()
        self.vista_registrazione.show()