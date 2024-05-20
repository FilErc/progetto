from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from listadipendente.controller.controller_lista_dipendente import ControllerListaDipendente
from utilizzatore.view.vista_inserisci_dipendente import VistaInserisciDipendente
from listadipendente.view.vista_dipendente import VistaDipendente

class VistaListaDipendente(QWidget):

    def __init__(self, parent=None):
        super(VistaListaDipendente, self).__init__(parent)
        uic.loadUi('listadipendente/view/lista_dipendente.ui', self)
        self.controller = ControllerListaDipendente()
        self.update_ui()
        self.open_button.clicked.connect(self.show_selected)
        self.new_button.clicked.connect(self.add_dipendente)
        self.delete_button.clicked.connect(self.delete)
        self.pushButton.clicked.connect(self.RicercaDipendente)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for dipendente in self.controller.get_lista_dipendente():
            item = QStandardItem()
            item.setText(f"{dipendente.cognome} {dipendente.nome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()

    def add_dipendente(self):
        self.vista_inserisci_dipendente = VistaInserisciDipendente(self.controller, self.update_ui)
        self.vista_inserisci_dipendente.show()

    def delete(self):
        lista = self.controller.ricercaDipendente(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.controller.rimuoviDipendente(lista[selected].cf)
            self.update_ui()

    def show_selected(self):
        lista = self.controller.ricercaDipendente(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.vista_dipendente = VistaDipendente(lista[selected])
            self.vista_dipendente.show()
            self.close()
    def RicercaDipendente(self):
        dipendente = self.lineEdit.text()
        lista = self.controller.ricercaDipendente(dipendente)
        self.listview_model = QStandardItemModel(self.list_view)
        for Dipendente in lista:
            item = QStandardItem()
            item.setText(f"{Dipendente.cognome} {Dipendente.nome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

