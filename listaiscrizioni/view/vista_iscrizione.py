from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from listaiscrizioni.controller.controller_lista_iscrizioni import ControllerListaIscrizioni

class VistaIscrizione(QWidget):
    def __init__(self, oggetto, parent=None):
        super(VistaIscrizione, self).__init__(parent)
        uic.loadUi('listaiscrizioni/view/vista_iscrizione.ui', self)
        self.controller = ControllerListaIscrizioni()
        self.labelCodice.setText(f"Codice: {self.controller.getCodice(oggetto)}")
        self.labelCliente.setText(f"CF cliente: {self.controller.getCliente(oggetto)}")
        self.labelAbbonamento.setText(f"Abbonamento: {self.controller.getAbbonamento(oggetto)}")
        self.labelDataInizio.setText(f"Data Inizio: {self.controller.getdataInizio(oggetto)}")
        self.labelDataFine.setText(f"Data Fine: {self.controller.getdataFine(oggetto)}")
