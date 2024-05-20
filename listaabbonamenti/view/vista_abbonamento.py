from PyQt6 import uic
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QWidget
from listaabbonamenti.controller.controller_lista_abbonamenti import ControllerListaAbbonamenti
class VistaAbbonamento(QWidget):
    def __init__(self, oggetto, parent=None):
        super(VistaAbbonamento, self).__init__(parent)
        uic.loadUi('listaabbonamenti/view/vista_abbonamento.ui', self)
        self.controller = ControllerListaAbbonamenti()
        self.labelCodice.setText(f"Codice: {self.controller.getCodice(oggetto)}")
        self.labelTipo.setText(f"{self.controller.getTipo(oggetto)}")
        self.labelCosto.setText(f"{self.controller.getCosto(oggetto)}")
        self.labelDurata.setText(f"{self.controller.getDurata(oggetto)}")
        self.labelCosto.setValidator(QIntValidator())
        self.labelDurata.setValidator(QIntValidator())
        self.pushButton.clicked.connect(lambda: self.salva(oggetto))
    def salva(self,abbonamento):
        self.controller.setInfoAbbonamento(abbonamento,self.labelCosto.text(),self.labelDurata.text())
        self.close()