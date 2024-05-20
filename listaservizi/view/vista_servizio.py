from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from listaservizi.controller.controller_lista_servizi import ControllerListaServizi
class VistaServizio(QWidget):
    def __init__(self, oggetto, parent=None):
        super(VistaServizio, self).__init__(parent)
        uic.loadUi('listaservizi/view/vista_servizio.ui', self)
        self.controller = ControllerListaServizi()
        self.labelCodice.setText(f"Codice: {self.controller.getCodice(oggetto)}")
        self.labelTipo.setText(f"{self.controller.getTipo(oggetto)}")