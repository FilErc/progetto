from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox
from listaiscrizioni.controller.controller_lista_iscrizioni import ControllerListaIscrizioni
from utilizzatore.view.vista_inserisci_iscrizioni import VistaInserisciIscrizioni
from listaiscrizioni.view.vista_iscrizione import VistaIscrizione
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
class VistaListaIscrizioni(QWidget):
    def __init__(self, parent=None):
        super(VistaListaIscrizioni, self).__init__(parent)
        uic.loadUi('listaiscrizioni/view/lista_iscrizioni.ui', self)
        self.controller = ControllerListaIscrizioni()
        self.listview_model = QStandardItemModel(self.list_view)
        self.list_view.setModel(self.listview_model)
        self.update_ui()
        self.open_button.clicked.connect(self.show_selected)
        self.open_button_2.clicked.connect(self.show_new_iscrizioni)
        self.open_button_3.clicked.connect(self.delete)
        self.pushButton.clicked.connect(self.RicercaIscrizione)
    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for iscrizioni in self.controller.get_lista_iscrizioni():
            item = QStandardItem()
            item.setText(f"{iscrizioni.codice}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
    def closeEvent(self, event):
        self.controller.save_data()
        super(VistaListaIscrizioni, self).closeEvent(event)
    def show_selected(self):
        lista = self.controller.ricercaIscrizione(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.vista_iscrizioni = VistaIscrizione(lista[selected])
            self.vista_iscrizioni.show()
    def show_new_iscrizioni(self):
        self.vista_inserisci_iscrizioni = VistaInserisciIscrizioni(self.controller, self.update_ui)
        self.vista_inserisci_iscrizioni.show()
    def delete(self):
        lista = self.controller.ricercaIscrizione(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.controller.rimuoviIscrizione(lista[selected].codice)
            self.update_ui()
    def RicercaIscrizione(self):
        iscrizione = self.lineEdit.text()
        lista = self.controller.ricercaIscrizione(iscrizione)
        self.listview_model = QStandardItemModel(self.list_view)
        for Iscrizione in lista:
            item = QStandardItem()
            item.setText(f"{Iscrizione.codice}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)