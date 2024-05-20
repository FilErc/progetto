from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from listacampi.controller.controller_lista_campi import ControllerListaCampi
class VistaCampo(QWidget):
    def __init__(self, oggetto, parent=None):
        super(VistaCampo, self).__init__(parent)
        uic.loadUi('listacampi/view/vista_campo.ui', self)
        self.controller = ControllerListaCampi()
        self.labelCodice.setText(f"Codice: {self.controller.getCodice(oggetto)}")
        self.labelTipo.setText(f"Tipo: {self.controller.getTipo(oggetto)}")
        self.labelDurataTurno.setText(f"Durata turno: {self.controller.getdurataTurno(oggetto)}")