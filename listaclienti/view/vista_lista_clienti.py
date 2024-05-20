from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
from utilizzatore.view.vista_inserisci_cliente import VistaInserisciCliente
from listaclienti.view.vista_cliente import VistaCliente
class VistaListaClienti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaClienti, self).__init__(parent)
        uic.loadUi('listaclienti/view/lista_clienti.ui', self)
        self.controller = ControllerListaClienti()
        self.update_ui()
        self.new_button.clicked.connect(self.add_cliente)
        self.open_button.clicked.connect(self.show_selected)
        self.delete_button.clicked.connect(self.delete)
        self.pushButton.clicked.connect(self.RicercaCliente)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.controller.get_lista_clienti():
            item = QStandardItem()
            item.setText(f"{cliente.cognome} {cliente.nome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
    def closeEvent(self, event):
        self.controller.save_data()
    def add_cliente(self):
        self.vista_inserisci_cliente = VistaInserisciCliente(self.controller, self.update_ui)
        self.vista_inserisci_cliente.show()
    def delete(self):
        lista = self.controller.bottoneRicercaCliente(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.controller.rimuoviCliente(lista[selected].cf)
            self.update_ui()
    def show_selected(self):
        lista = self.controller.bottoneRicercaCliente(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.vista_cliente = VistaCliente(lista[selected])
            self.vista_cliente.show()
            self.close()
    def RicercaCliente(self):
        cliente = self.lineEdit.text()
        lista = self.controller.bottoneRicercaCliente(cliente)
        self.listview_model = QStandardItemModel(self.list_view)
        for Cliente in lista:
            item = QStandardItem()
            item.setText(f"{Cliente.cognome} {Cliente.nome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)