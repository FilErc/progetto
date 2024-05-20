from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from listaprenotazioni.controller.controller_lista_prenotazioni import ControllerListaPrenotazioni
class VistaPrenotazione(QWidget):
    def __init__(self, oggetto, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        uic.loadUi('listaprenotazioni/view/vista_prenotazione.ui', self)
        self.controller = ControllerListaPrenotazioni()
        campo = self.controller.getCampo(oggetto).split("_")
        self.labelCodice.setText(f" {self.controller.getCodice(oggetto)}")
        self.labelCampo.setText(f"Campo: {campo[0]}")
        self.labelOrario.setText(f"Orario: {self.controller.getOrario(oggetto)}")
        self.labelAssegnamento.setText(f"Assegnamento: {self.controller.getAssegnamento(oggetto)}")
        self.labelCliente.setText(f"Cliente: {self.controller.getCliente(oggetto)}")
        self.labelData.setText(f"Data: {self.controller.getData(oggetto)}")
