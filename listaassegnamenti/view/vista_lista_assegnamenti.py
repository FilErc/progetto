from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox
from listaassegnamenti.controller.controller_lista_assegnamenti import ControllerListaAssegnamenti
from listaprenotazioni.controller.controller_lista_prenotazioni import ControllerListaPrenotazioni
from utilizzatore.view.vista_inserisci_assegnamenti import VistaInserisciAssegnamenti
from listaassegnamenti.view.vista_assegnamento import VistaAssegnamento
class VistaListaAssegnamenti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaAssegnamenti, self).__init__(parent)
        uic.loadUi('listaassegnamenti/view/lista_assegnamenti.ui', self)
        self.controller = ControllerListaAssegnamenti()
        self.controllorePrenotazioni = ControllerListaPrenotazioni()
        self.listview_model = QStandardItemModel(self.list_view)
        self.list_view.setModel(self.listview_model)
        self.update_ui()
        self.open_button.clicked.connect(self.show_selected)
        self.open_button_2.clicked.connect(self.show_new_assegnamenti)
        self.open_button_3.clicked.connect(self.delete)
        self.pushButton.clicked.connect(self.RicercaAssegnamento)
    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for assegnamenti in self.controller.get_lista_assegnamenti():
            item = QStandardItem()
            item.setText(f"{assegnamenti.codice}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
    def closeEvent(self, event):
        self.controller.save_data()
        super(VistaListaAssegnamenti, self).closeEvent(event)
    def show_selected(self):
        lista = self.controller.ricercaAssegnamento(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.vista_assegnamenti = VistaAssegnamento(lista[selected])
            self.vista_assegnamenti.show()
    def show_new_assegnamenti(self):
        prenotazione = None
        self.vista_inserisci_assegnamenti = VistaInserisciAssegnamenti(None, self.controller, self.update_ui, prenotazione)
        self.vista_inserisci_assegnamenti.show()
    def delete(self):
        lista = self.controller.ricercaAssegnamento(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            for p in self.controllorePrenotazioni.get_lista_prenotazioni():
                if p.codice == lista[selected].prenotazione:
                    self.controllorePrenotazioni.setAssegnamento(p, "")
            self.controller.rimuoviAssegnamento(lista[selected].codice)
            self.update_ui()
    def RicercaAssegnamento(self):
        assegnamento = self.lineEdit.text()
        lista = self.controller.ricercaAssegnamento(assegnamento)
        self.listview_model = QStandardItemModel(self.list_view)
        for Assegnamento in lista:
            item = QStandardItem()
            item.setText(f"{Assegnamento.codice}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
