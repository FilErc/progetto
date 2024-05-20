from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QScrollArea, QMessageBox

from obj.Prenotazione import Prenotazione
from datetime import datetime, timedelta
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
from listacampi.controller.controller_lista_campi import ControllerListaCampi
from listaprenotazioni.controller.controller_lista_prenotazioni import ControllerListaPrenotazioni
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QColor
from listaassegnamenti.controller.controller_lista_assegnamenti import ControllerListaAssegnamenti
from utilizzatore.view.vista_inserisci_assegnamenti import VistaInserisciAssegnamenti
from listaservizi.view.vista_lista_servizi import VistaListaServizi
class VistaInserisciPrenotazione(QWidget):


    def __init__(self, controller, callback, HomeDipendente, parent=None):
        super(VistaInserisciPrenotazione, self).__init__(parent)
        uic.loadUi('utilizzatore/view/vista_inserisci_prenotazione.ui', self)
        self.controller = controller
        self.callback = callback
        max_date = QDate.currentDate().addDays(30)
        self.calendarWidget.setMaximumDate(max_date)
        min_date = QDate.currentDate()
        self.calendarWidget.setMinimumDate(min_date)
        self.RicercaButton_Cliente.clicked.connect(self.RicercaCliente)
        self.RicercaButton_Campo.clicked.connect(self.RicercaCampo)
        self.btn_ok.clicked.connect(self.SceltaOrario)
        self.Conferma_button.clicked.connect(lambda: self.add_prenotazioni(False, HomeDipendente))
        self.Conferma_assegnamento.clicked.connect(lambda: self.add_prenotazioni(True, HomeDipendente))
    def update_ui_clienti(self):
        self.controlloreCliente = ControllerListaClienti()
        self.listview_model = QStandardItemModel(self.listViewClienti)
        for cliente in self.controlloreCliente.get_lista_clienti():
            item = QStandardItem()
            item.setText(f"{cliente.nome} {cliente.cognome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listViewClienti.setModel(self.listview_model)
    def update_ui_campi(self):
        self.controlloreCampo = ControllerListaCampi()
        self.listview_model = QStandardItemModel(self.listViewCampi)
        for campo in self.controlloreCampo.get_lista_campi():
            item = QStandardItem()
            item.setText(f"{campo.codice}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listViewCampi.setModel(self.listview_model)
    def RicercaCliente(self):
        cliente = self.textCliente.text()
        self.controlloreCliente = ControllerListaClienti()
        lista = self.controlloreCliente.bottoneRicercaCliente(cliente)
        self.listview_model = QStandardItemModel(self.listViewClienti)
        for clienti in lista:
            item = QStandardItem()
            if clienti.iscrizione != "":
                item.setText(f"{clienti.nome} {clienti.cognome}")
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
            else:
                item.setText(f"{clienti.nome} {clienti.cognome}")
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                color = QColor(255, 0, 0)
                item.setForeground(color)
                item.setSelectable(False)
            self.listview_model.appendRow(item)
        self.listViewClienti.setModel(self.listview_model)
    def RicercaCampo(self):
        if self.listViewClienti.selectedIndexes():
            self.controlloreCampo = ControllerListaCampi()
            campo = self.textCampo.text()
            lista = self.controlloreCampo.CreaLista(campo)
            self.listview_model = QStandardItemModel(self.listViewCampi)
            for campo in lista:
                item = QStandardItem()
                item.setText(f"{campo.codice}")
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.listview_model.appendRow(item)
            self.listViewCampi.setModel(self.listview_model)

    def SceltaOrario(self):
        selected_indexes_campo = self.listViewCampi.selectedIndexes()
        data_selezionata = self.calendarWidget.selectedDate()
        if data_selezionata and selected_indexes_campo:
            self.controlloreCampo = ControllerListaCampi()
            campo = self.textCampo.text()
            lista, campo_selezionato = self.controlloreCampo.CrealistaFinale1(selected_indexes_campo, campo)
            self.controllorePrenotazione = ControllerListaPrenotazioni()
            lista_finale = self.controllorePrenotazione.CreaListaFinale2(lista, campo_selezionato, data_selezionata)
            self.listview_model = QStandardItemModel(self.listViewOrari)
            for turno in lista_finale:
                    item = QStandardItem()
                    item.setText(f"{turno}")
                    item.setEditable(False)
                    font = item.font()
                    font.setPointSize(18)
                    item.setFont(font)
                    self.listview_model.appendRow(item)
            self.listViewOrari.setModel(self.listview_model)

    def add_prenotazioni(self, bool, HomeDipendente):
        if self.listViewClienti.selectedIndexes() and self.listViewCampi.selectedIndexes() and self.calendarWidget.selectedDate() and self.listViewOrari.selectedIndexes():
            year = self.calendarWidget.selectedDate().year()
            if QDate(year, 6, 1) <= self.calendarWidget.selectedDate() <= QDate(year, 8, 31) and HomeDipendente:
                msg = QMessageBox(
                    text="Errore!",
                    parent=None)
                msg.setIcon(QMessageBox.Icon.Question)
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.setInformativeText("")
                msg.setWindowTitle("Errore!")
                msg.exec()
            else:
                self.controlloreClienti = ControllerListaClienti()
                self.controlloreCampo = ControllerListaCampi()
                campo = self.textCampo.text()
                selected_indexes_cliente = self.listViewClienti.selectedIndexes()
                selected = selected_indexes_cliente[0].row()
                lista_clienti = self.controlloreClienti.bottoneRicercaCliente(self.textCliente.text())
                cliente = lista_clienti[selected].cf
                selected_indexes_campo = self.listViewCampi.selectedIndexes()
                data_selezionata = self.calendarWidget.selectedDate()
                selected_date = data_selezionata.toString("yyyy-MM-dd")
                lista, campo_selezionato = self.controlloreCampo.CrealistaFinale1(selected_indexes_campo, campo)
                self.controllorePrenotazione = ControllerListaPrenotazioni()
                lista_finale = self.controllorePrenotazione.CreaListaFinale2(lista, campo_selezionato, data_selezionata)
                selected_indexes_orario = self.listViewOrari.selectedIndexes()
                if selected_indexes_orario:
                    selectedOrario = selected_indexes_orario[0].row()
                    orario_selezionato = lista_finale[selectedOrario]
                id = "_" + str(self.controller.id_chooser())
                campo = campo_selezionato.codice
                orario = orario_selezionato
                assegnamento = ""
                data = selected_date
                self.controller.aggiungi_prenotazione(Prenotazione
                                                      ((cliente + id).lower(),
                                                       campo,
                                                       orario,
                                                       assegnamento,
                                                       data,
                                                       cliente))
                self.callback()
                self.close()
                if bool:
                    self.controllerAssegnamenti = ControllerListaAssegnamenti()
                    self.vista_inserisci_assegnamenti = VistaInserisciAssegnamenti(self.callback,
                                                                                   self.controllerAssegnamenti, None,
                                                                                   (cliente + id).lower())
                    self.vista_inserisci_assegnamenti.show()
        else:
            msg = QMessageBox(
                text="Errore!",
                parent=None)
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setInformativeText("")
            msg.setWindowTitle("Errore!")
            msg.exec()