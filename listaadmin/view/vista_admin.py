from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from listaadmin.controller.controller_lista_admin import ControllerListaAdmin
class VistaAdmin(QWidget):
    def __init__(self, oggetto, parent=None):
        super(VistaAdmin, self).__init__(parent)
        uic.loadUi('listaadmin/view/vista_admin.ui', self)
        self.controller = ControllerListaAdmin()
        self.labelNomeCognome.setText(f"{self.controller.getNome(oggetto)} {self.controller.getCognome(oggetto)}")
        self.labelCF.setText(f"{self.controller.getCF(oggetto)}")
        self.labelCF.setReadOnly(True)
        self.labelIndirizzo.setText(f"{self.controller.getIndirizzo(oggetto)}")
        self.labelEmail.setText(f"{self.controller.getEmail(oggetto)}")
        self.labelTelefono.setText(f"{self.controller.getTelefono(oggetto)}")
        self.pushButton.clicked.connect(self.modifica)
        self.rimuoviProfilo.clicked.connect(lambda: self.rimuovi(oggetto))
    def modifica(self):
        self.controller.setInfoAdmin(self.labelCF.text(),self.labelEmail.text(),self.labelIndirizzo.text(),self.labelTelefono.text())
        self.close()
    def rimuovi(self,oggetto):
        with open("listautenti/data/lista_utenti.txt", 'r') as file:
            righe = file.readlines()
        righe_filtrate = [riga for riga in righe if not riga.startswith(oggetto.cf + ':')]
        with open("listautenti/data/lista_utenti.txt", 'w') as file:
            file.writelines(righe_filtrate)
        self.close()