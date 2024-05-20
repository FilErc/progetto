from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from listaprenotazioni.controller.controller_lista_prenotazioni import ControllerListaPrenotazioni
from utilizzatore.view.vista_inserisci_prenotazione import VistaInserisciPrenotazione
from listaclienti.model.lista_clienti import ListaClienti
from listacampi.controller.controller_lista_campi import ControllerListaCampi
from listaassegnamenti.controller.controller_lista_assegnamenti import ControllerListaAssegnamenti
from listaprenotazioni.view.vista_prenotazione import VistaPrenotazione
class VistaListaPrenotazioni(QWidget):
    def __init__(self,HomeDipendente, parent=None):
        super(VistaListaPrenotazioni, self).__init__(parent)
        uic.loadUi('listaprenotazioni/view/lista_prenotazioni.ui', self)
        self.controller = ControllerListaPrenotazioni()
        self.controllerCliente = ListaClienti()
        self.controlloreCampi = ControllerListaCampi()
        self.controlloreAssegnamenti = ControllerListaAssegnamenti()
        self.listview_model = QStandardItemModel(self.list_view)
        self.list_view.setModel(self.listview_model)
        self.update_ui()
        self.open_button.clicked.connect(self.show_selected)
        self.open_button_2.clicked.connect(lambda: self.show_new_prenotazione(HomeDipendente))
        self.RicercaButton_Prenotazione.clicked.connect(self.RicercaPrenotazione)
        self.open_button_3.clicked.connect(self.delete)
    def RicercaPrenotazione(self):
        prenotazione = self.textPrenotazione.text()
        lista = self.controller.bottoneRicercaPrenotazioni(prenotazione)
        self.listview_model = QStandardItemModel(self.list_view)
        for Prenotazioni in lista:
            item = QStandardItem()
            item.setText(f"{Prenotazioni.codice}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for prenotazione in self.controller.get_lista_prenotazioni():
            item = QStandardItem()
            item.setText(f"{prenotazione.codice}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
    def closeEvent(self, event):
        self.controller.save_data()
        super(VistaListaPrenotazioni, self).closeEvent(event)
    def show_selected(self):
        lista = self.controller.bottoneRicercaPrenotazioni(self.textPrenotazione.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            self.vista_prenotazione = VistaPrenotazione(lista[selected])
            self.vista_prenotazione.show()
    def show_new_prenotazione(self, HomeDipendente):
        self.vista_inserisci_prenotazione = VistaInserisciPrenotazione(self.controller, self.update_ui, HomeDipendente)
        self.vista_inserisci_prenotazione.show()
        self.close()
    def delete(self):
        lista = self.controller.bottoneRicercaPrenotazioni(self.textPrenotazione.text())
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            selected = selected_indexes[0].row()
            for p in self.controller.get_lista_prenotazioni():
                if p.codice == lista[selected].codice:
                    self.controlloreAssegnamenti.rimuoviAssegnamento(lista[selected].assegnamento)
            self.controller.rimuoviPrenotazione(lista[selected].codice)
        self.update_ui()