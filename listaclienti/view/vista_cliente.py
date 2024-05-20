from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
class VistaCliente(QWidget):
    def __init__(self, oggetto, parent=None):
        super(VistaCliente, self).__init__(parent)
        uic.loadUi('listaclienti/view/vista_cliente.ui', self)
        self.controller = ControllerListaClienti()
        self.labelNomeCognome.setText(f"{self.controller.getNome(oggetto)} {self.controller.getCognome(oggetto)}")
        self.labelCF.setText(f"{self.controller.getCF(oggetto)}")
        self.labelCF.setReadOnly(True)
        self.labelIndirizzo.setText(f"{self.controller.getIndirizzo(oggetto)}")
        self.labelEmail.setText(f"{self.controller.getEmail(oggetto)}")
        self.labelTelefono.setText(f"{self.controller.getTelefono(oggetto)}")
        self.labelIscrizione.setText(f"{self.controller.getIscrizione(oggetto)}")
        self.labelIscrizione.setReadOnly(True)
        self.pushButton.clicked.connect(self.modifica)
        self.rimuoviProfilo.clicked.connect(lambda: self.rimuovi(oggetto))

    def modifica(self):
        self.controller.setInfoCliente(self.labelCF.text(), self.labelEmail.text(), self.labelIndirizzo.text(),
                                          self.labelTelefono.text())
        self.close()
    def rimuovi(self,oggetto):
        with open("listautenti/data/lista_utenti.txt", 'r') as file:
            righe = file.readlines()
        righe_filtrate = [riga for riga in righe if not riga.startswith(oggetto.cf + ':')]
        with open("listautenti/data/lista_utenti.txt", 'w') as file:
            file.writelines(righe_filtrate)
        self.close()
