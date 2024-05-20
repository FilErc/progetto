from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox
from listaabbonamenti.controller.controller_lista_abbonamenti import ControllerListaAbbonamenti
from utilizzatore.view.vista_inserisci_abbonamenti import VistaInserisciAbbonamenti
from listaabbonamenti.view.vista_abbonamento import VistaAbbonamento
class VistaListaAbbonamenti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaAbbonamenti, self).__init__(parent)
        uic.loadUi('listaabbonamenti/view/lista_abbonamenti.ui', self)
        self.controller = ControllerListaAbbonamenti()
        self.listview_model = QStandardItemModel(self.list_view)
        self.list_view.setModel(self.listview_model)
        self.update_ui()
        self.open_button.clicked.connect(self.show_selected)
        self.open_button_2.clicked.connect(self.show_new_abbonamenti)
        self.open_button_3.clicked.connect(self.delete)
        self.pushButton.clicked.connect(self.RicercaAbbonamento)
    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for abbonamenti in self.controller.get_lista_abbonamenti():
            item = QStandardItem()
            item.setText(f"{abbonamenti.codice}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
    def closeEvent(self, event):
        self.controller.save_data()
        super(VistaListaAbbonamenti, self).closeEvent(event)
    def show_new_abbonamenti(self):
        self.vista_inserisci_abbonamenti = VistaInserisciAbbonamenti(self.controller, self.update_ui)
        self.vista_inserisci_abbonamenti.show()
    def delete(self):
        lista = self.controller.ricercaAbbonamento(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.controller.rimuoviAbbonamento(lista[selected].codice)
        self.update_ui()
    def RicercaAbbonamento(self):
        abbonamento = self.lineEdit.text()
        lista = self.controller.ricercaAbbonamento(abbonamento)
        self.listview_model = QStandardItemModel(self.list_view)
        for Abbonamento in lista:
            item = QStandardItem()
            item.setText(f"{Abbonamento.codice}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
    def show_selected(self):
        lista = self.controller.ricercaAbbonamento(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.vista_abbonamenti = VistaAbbonamento(lista[selected])
            self.vista_abbonamenti.show()