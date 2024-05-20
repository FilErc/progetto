from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtWidgets import QApplication, QTextBrowser
from sistema.Statistiche import GestoreStatistiche
class VistaListaStatistiche(QWidget):
    def __init__(self, parent=None):
        super(VistaListaStatistiche, self).__init__(parent)
        uic.loadUi('utilizzatore/view/Statistiche.ui', self)
        self.controller = GestoreStatistiche()
        self.numeroClienti.setText(f"Numero Clienti: {self.controller.NumeroClienti()}")
        print(1)
        self.numeroDipendenti.setText(f"Numero Dipendenti: {self.controller.NumeroDipendenti()}")
        print(1)
        self.numeroAdmin.setText(f"Numero Admin: {self.controller.NumeroAdmin()}")
        print(1)
        self.numeroAbbonamenti.setText(f"Numero Abbonamenti: {self.controller.NumeroAbbonamenti()}")
        print(1)
        self.numeroAssegnamenti.setText(f"Numero Assegnamenti: {self.controller.NumeroAssegnamenti()}")
        print(1)
        self.numeroCampi.setText(f"Numero Campi: {self.controller.NumeroCampi()}")
        print(1)
        self.numeroIscrizioni.setText(f"Numero Iscrizioni: {self.controller.NumeroIscrizioni()}")
        print(1)
        self.numeroPrenotazioni.setText(f"Numero Prenotazioni: {self.controller.NumeroPrenotazioni()}")
        print(1)
        self.numeroServizi.setText(f"Numero Servizi: {self.controller.NumeroServizi()}")
        print(1)
        self.ClassificaCampi.setPlainText(str(self.controller.ClassificaCampiScelti()))
        print(1)
        self.ClassificaServizi.setPlainText(self.controller.ClassificaServiziScelti())
        print(1)
        self.ClassificaAbbonamenti.setPlainText(self.controller.ClassificaAbbonamentiScelti())
        print(1)

