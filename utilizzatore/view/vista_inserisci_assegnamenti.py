from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox
from listaprenotazioni.controller.controller_lista_prenotazioni import ControllerListaPrenotazioni
from listaservizi.controller.controller_lista_servizi import ControllerListaServizi
from obj.Assegnamenti import Assegnamenti
class VistaInserisciAssegnamenti(QWidget):

    def __init__(self, callbackPrenotazioni, controller, callback, prenotazione, parent=None):
        super(VistaInserisciAssegnamenti, self).__init__(parent)
        uic.loadUi('utilizzatore/view/vista_inserisci_assegnamenti.ui', self)
        self.controller = controller
        self.callback = callback
        self.callbackPre = callbackPrenotazioni
        self.listview_model_servizi = QStandardItemModel(self.listViewServizi)
        self.listViewServizi.setModel(self.listview_model_servizi)
        self.update_servizi()
        if prenotazione is not None:
            self.RicercaPrenotazioni(prenotazione)#aggiunto per aggiornare la lista delle prenotazioni visualizzata quando si arriva qui passando dal bottone aggiungi assegnamento in prenotazioni
            self.textPrenotazioni.setReadOnly(True)
            self.RicercaButton.setEnabled(False)
            self.RicercaPrenotazioni(prenotazione)
        else:
            self.listview_model_Prenotazioni = QStandardItemModel(self.listViewPrenotazioni)
            self.listViewPrenotazioni.setModel(self.listview_model_Prenotazioni)
            self.update_prenotazioni()
        self.RicercaButton.clicked.connect(lambda: self.RicercaPrenotazioni(prenotazione))
        self.RicercaButton_Servizi.clicked.connect(self.RicercaServizi)
        self.btn_ok.clicked.connect(lambda: self.add_assegnamento(prenotazione))
    def update_servizi(self):
        self.listview_model = QStandardItemModel(self.listViewServizi)
        self.controllerServizi = ControllerListaServizi()
        for servizi in self.controllerServizi.get_lista_servizi():
            item = QStandardItem()
            item.setText(f"{servizi.tipo}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listViewServizi.setModel(self.listview_model)
    def update_prenotazioni(self):
        self.listview_model = QStandardItemModel(self.listViewPrenotazioni)
        self.controllerPrenotazioni = ControllerListaPrenotazioni()
        lista = []
        for p in self.controllerPrenotazioni.get_lista_prenotazioni():
            if p.assegnamento == "":
                lista.append(p)
        for Prenotazioni in lista:
            item = QStandardItem()
            item.setText(f"{Prenotazioni.codice}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listViewPrenotazioni.setModel(self.listview_model)
    def RicercaPrenotazioni(self, Prenotazioni):#Rinominarla con update_ricercaPrenotazioni?
        if Prenotazioni is None: #nel caso in cui si aggiunga l'assegnamento tramite la prenotazione serve sennò la lista è impossibile da aggiornare e fa vedere tutti gli elementi in lista
            Prenotazioni = self.textPrenotazioni.text()
        self.controllorePrenotazioni = ControllerListaPrenotazioni()
        lista2 = self.controllorePrenotazioni.bottoneRicercaPrenotazioni(Prenotazioni)
        lista = []
        for p in lista2:
            if p.assegnamento == "":
                lista.append(p)
        self.listview_model = QStandardItemModel(self.listViewPrenotazioni)
        for Prenotazioni in lista:
            item = QStandardItem()
            item.setText(f"{Prenotazioni.codice}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listViewPrenotazioni.setModel(self.listview_model)
    def RicercaServizi(self):
        Servizi = self.textServizio.text()
        self.controlloreServizi = ControllerListaServizi()
        lista = self.controlloreServizi.bottoneRicercaServizi(Servizi)
        self.listview_model = QStandardItemModel(self.listViewServizi)
        for Servizi in lista:
            item = QStandardItem()
            item.setText(f"{Servizi.tipo}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listViewServizi.setModel(self.listview_model)
    def add_assegnamento(self, codicePre):
        selected_indexes_servizio = self.listViewServizi.selectedIndexes()
        selected_indexes_prenotazioni = self.listViewPrenotazioni.selectedIndexes()
        if selected_indexes_prenotazioni and selected_indexes_servizio:
            self.controllorePrenotazioni = ControllerListaPrenotazioni()
            Pre = self.textPrenotazioni.text()
            lista2 = self.controllorePrenotazioni.ricercaPrenotazione(Pre)
            lista = []
            for p in lista2:
                if p.assegnamento == "":
                    lista.append(p)
            self.controlloreServizi = ControllerListaServizi()
            Ser = self.textServizio.text()
            listaSer = self.controlloreServizi.ricercaServizioTipo(Ser)
            if selected_indexes_prenotazioni:  # Conversione listobject to object
                selectedPrenotazione = selected_indexes_prenotazioni[0].row()
            if selected_indexes_servizio:  # Conversione listobject to object
                selectedServizio = selected_indexes_servizio[0].row()
            id = "_" + str(self.controller.id_chooser())
            if codicePre is None:
                prenotazione = self.controllorePrenotazioni.getCodice(lista[selectedPrenotazione])
                cliente = self.controllorePrenotazioni.getCliente(lista[selectedPrenotazione])
                self.controllorePrenotazioni.setAssegnamento(lista[selectedPrenotazione], prenotazione + id)
            else:
                prenotazione = codicePre
                for p in self.controllorePrenotazioni.get_lista_prenotazioni():
                    if p.codice == codicePre:
                        cod = prenotazione + id
                        self.controllorePrenotazioni.setAssegnamento(p, cod)
                        cliente = p.cliente
            if self.callbackPre is not None:
                self.callbackPre()
            servizio = self.controlloreServizi.getTipo(listaSer[selectedServizio])
            self.controller.aggiungi_assegnamenti(Assegnamenti
                                                  ((prenotazione + id).lower(),
                                                   cliente,
                                                   prenotazione,
                                                   servizio))
            if self.callback is not None:
                self.callback()
            self.close()
        elif codicePre and selected_indexes_servizio:
            self.controllorePrenotazioni = ControllerListaPrenotazioni()
            self.controlloreServizi = ControllerListaServizi()
            if selected_indexes_prenotazioni:  # Conversione listobject to object
                selectedPrenotazione = selected_indexes_prenotazioni[0].row()
                prenotazione_selezionato = self.controllorePrenotazioni.get_prenotazione_by_index(selectedPrenotazione)
            if selected_indexes_servizio:  # Conversione listobject to object
                selectedServizio = selected_indexes_servizio[0].row()
                servizio_selezionato = self.controlloreServizi.get_servizio_by_index(selectedServizio)
            id = "_" + str(self.controller.id_chooser())
            if codicePre is None:
                prenotazione = self.controllorePrenotazioni.getCodice(prenotazione_selezionato)
                cliente = self.controllorePrenotazioni.getCliente(prenotazione_selezionato)
                self.controllorePrenotazioni.setAssegnamento(prenotazione_selezionato, prenotazione + id)
            else:
                prenotazione = codicePre
                for p in self.controllorePrenotazioni.get_lista_prenotazioni():
                    if p.codice == codicePre:
                        cod = prenotazione + id
                        self.controllorePrenotazioni.setAssegnamento(p, cod)
                        cliente = p.cliente
            if self.callbackPre is not None:
                self.callbackPre()
            servizio = self.controlloreServizi.getTipo(servizio_selezionato)
            self.controller.aggiungi_assegnamenti(Assegnamenti
                                                  ((prenotazione + id).lower(),
                                                   cliente,
                                                   prenotazione,
                                                   servizio))
            if self.callback is not None:
                self.callback()
            self.close()
        else:
            msg = QMessageBox(
                text="Errore!",
                parent=None)
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setInformativeText("")
            msg.setWindowTitle("Errore!")
            msg.exec()
