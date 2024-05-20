from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget
from listaadmin.controller.controller_lista_admin import ControllerListaAdmin
from utilizzatore.view.vista_inserisci_admin import VistaInserisciAdmin
from listaadmin.view.vista_admin import VistaAdmin
class VistaListaAdmin(QWidget):
    def __init__(self, parent=None):
        super(VistaListaAdmin, self).__init__(parent)
        uic.loadUi('listaadmin/view/lista_admin.ui', self)
        self.controller = ControllerListaAdmin()
        self.update_ui()
        self.open_button.clicked.connect(self.show_selected)
        self.new_button.clicked.connect(self.add_admin)
        self.delete_button.clicked.connect(self.delete)
        self.pushButton.clicked.connect(self.RicercaAdmin)
    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for admin in self.controller.get_lista_admin():
            item = QStandardItem()
            item.setText(f"{admin.cognome} {admin.nome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()
    def add_admin(self):
        self.vista_inserisci_admin = VistaInserisciAdmin(self.controller, self.update_ui)
        self.vista_inserisci_admin.show()
    def delete(self):
        lista = self.controller.ricercaAdmin(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.controller.rimuoviAdmin(lista[selected].cf)
            self.update_ui()
    def show_selected(self):
        lista = self.controller.ricercaAdmin(self.lineEdit.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.vista_admin = VistaAdmin(lista[selected])
            self.vista_admin.show()
            self.close()
    def RicercaAdmin(self):
        admin = self.lineEdit.text()
        lista = self.controller.ricercaAdmin(admin)
        self.listview_model = QStandardItemModel(self.list_view)
        for Admin in lista:
            item = QStandardItem()
            item.setText(f"{Admin.cognome} {Admin.nome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)