from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from listaservizi.controller.controller_lista_servizi import ControllerListaServizi
from utilizzatore.view.vista_inserisci_servizio import VistaInserisciServizio
from listaservizi.view.vista_servizio import VistaServizio


class VistaListaServizi(QWidget):

    def __init__(self, parent=None):
        super(VistaListaServizi, self).__init__(parent)
        uic.loadUi('listaservizi/view/lista_servizi.ui', self)

        self.controller = ControllerListaServizi()

        self.listview_model = QStandardItemModel(self.list_view)
        self.list_view.setModel(self.listview_model)
        self.update_ui()

        self.open_button.clicked.connect(self.show_selected)
        self.open_button_2.clicked.connect(self.show_new_servizio)
        self.open_button_3.clicked.connect(self.delete)
        self.pushButton.clicked.connect(self.RicercaServizio)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for servizio in self.controller.get_lista_servizi():
            item = QStandardItem()
            item.setText(f"{servizio.tipo}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


    def closeEvent(self, event):
        self.controller.save_data()
        super(VistaListaServizi, self).closeEvent(event)

    def show_selected(self):
        lista = self.controller.ricercaServizioTipo(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.vista_servizio = VistaServizio(lista[selected])
            self.vista_servizio.show()

    def show_new_servizio(self):
        self.vista_inserisci_servizio = VistaInserisciServizio(self.controller, self.update_ui)
        self.vista_inserisci_servizio.show()

    def delete(self):
        lista = self.controller.ricercaServizioTipo(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.controller.rimuoviServizio(lista[selected].codice)
            self.update_ui()
    def RicercaServizio(self):
        servizio = self.lineEdit.text()
        lista = self.controller.ricercaServizioTipo(servizio)
        self.listview_model = QStandardItemModel(self.list_view)
        for Servizio in lista:
            item = QStandardItem()
            item.setText(f"{Servizio.codice}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)




