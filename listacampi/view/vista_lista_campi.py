from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from listacampi.controller.controller_lista_campi import ControllerListaCampi
from utilizzatore.view.vista_inserisci_campi import VistaInserisciCampi
from listacampi.view.vista_campo import VistaCampo


class VistaListaCampi(QWidget):

    def __init__(self, parent=None):
        super(VistaListaCampi, self).__init__(parent)
        uic.loadUi('listacampi/view/lista_campi.ui', self)

        self.controller = ControllerListaCampi()

        self.listview_model = QStandardItemModel(self.list_view)
        self.list_view.setModel(self.listview_model)
        self.update_ui()
        self.open_button.clicked.connect(self.show_selected)
        self.open_button_2.clicked.connect(self.show_new_campi)
        self.open_button_3.clicked.connect(self.delete)
        self.pushButton.clicked.connect(self.RicercaCampo)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for campi in self.controller.get_lista_campi():
            item = QStandardItem()
            item.setText(f"{campi.codice}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


    def closeEvent(self, event):
        self.controller.save_data()
        super(VistaListaCampi, self).closeEvent(event)

    def show_selected(self):
        lista = self.controller.ricercaCampoTipo(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.vista_campi = VistaCampo(lista[selected])
            self.vista_campi.show()

    def show_new_campi(self):
        self.vista_inserisci_campi = VistaInserisciCampi(self.controller, self.update_ui)
        self.vista_inserisci_campi.show()

    def delete(self):
        lista = self.controller.ricercaCampoTipo(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.controller.rimuoviCampo(lista[selected].codice)
            self.update_ui()
    def RicercaCampo(self):
        campo = self.lineEdit.text()
        lista = self.controller.ricercaCampoTipo(campo)
        self.listview_model = QStandardItemModel(self.list_view)
        for Campo in lista:
            item = QStandardItem()
            item.setText(f"{Campo.codice}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)




