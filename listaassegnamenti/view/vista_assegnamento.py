from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from listaassegnamenti.controller.controller_lista_assegnamenti import ControllerListaAssegnamenti

class VistaAssegnamento(QWidget):
    def __init__(self, oggetto, parent=None):
        super(VistaAssegnamento, self).__init__(parent)
        uic.loadUi('listaassegnamenti/view/vista_assegnamento.ui', self)
        self.controller = ControllerListaAssegnamenti()
        self.labelCodice.setText(f"{self.controller.getCodice(oggetto)}")
        self.labelCliente.setText(f"Cliente: {self.controller.getCliente(oggetto)}")
        self.labelPrenotazione.setText(f"Codice prenotazione: {self.controller.getPrenotazione(oggetto)}")
        self.labelServizio.setText(f"Codice servizio: {self.controller.getServizio(oggetto)}")