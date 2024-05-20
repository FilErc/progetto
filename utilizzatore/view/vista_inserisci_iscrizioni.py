from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtGui import QIntValidator
import datetime
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
from listaabbonamenti.controller.controller_lista_abbonamenti import ControllerListaAbbonamenti
from obj.Iscrizioni import Iscrizioni


class VistaInserisciIscrizioni(QWidget):

    def __init__(self, controller, callback, parent=None):
        super(VistaInserisciIscrizioni, self).__init__(parent)
        uic.loadUi('utilizzatore/view/vista_inserisci_iscrizioni.ui', self)
        self.controller = controller
        self.callback = callback
        self.listview_model_Abbonamenti = QStandardItemModel(self.listViewAbbonamenti)
        self.listViewAbbonamenti.setModel(self.listview_model_Abbonamenti)
        self.update_abbonamenti()
        self.listview_model_Clienti = QStandardItemModel(self.listViewClienti)
        self.listViewClienti.setModel(self.listview_model_Clienti)
        self.update_clienti()
        self.RicercaButton.clicked.connect(self.RicercaCliente)
        self.btn_ok.clicked.connect(self.add_iscrizioni)
    def update_abbonamenti(self):
        self.listview_model = QStandardItemModel(self.listViewAbbonamenti)
        self.controllerAbb = ControllerListaAbbonamenti()
        for abbonamenti in self.controllerAbb.get_lista_abbonamenti():
            item = QStandardItem()
            item.setText(f"{abbonamenti.tipo}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listViewAbbonamenti.setModel(self.listview_model)
    def update_clienti(self):
        self.listview_model = QStandardItemModel(self.listViewClienti)
        self.controllerClienti = ControllerListaClienti()
        lista = []
        for c in self.controllerClienti.get_lista_clienti():
            if c.iscrizione == "":
                lista.append(c)
        for clienti in lista:
            item = QStandardItem()
            item.setText(f"{clienti.nome} {clienti.cognome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listViewClienti.setModel(self.listview_model)

    def RicercaCliente(self):
        cliente = self.textCliente.text()
        self.controlloreCliente = ControllerListaClienti()
        lista2 = self.controlloreCliente.bottoneRicercaCliente(cliente)
        self.listview_model = QStandardItemModel(self.listViewClienti)
        lista = []
        for c in lista2:
            if c.iscrizione == "":
                lista.append(c)
        for clienti in lista:
            item = QStandardItem()
            item.setText(f"{clienti.nome} {clienti.cognome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listViewClienti.setModel(self.listview_model)

    def add_iscrizioni(self):
        bool1 = True
        bool2 = True
        self.controlloreClienti = ControllerListaClienti()
        self.controlloreAbbonamento = ControllerListaAbbonamenti()
        testo = self.textCliente.text()
        lista2 = self.controlloreClienti.bottoneRicercaCliente(testo)
        lista = []
        for c in lista2:
           if c.iscrizione == "":
             lista.append(c)
        selected_indexes_cliente = self.listViewClienti.selectedIndexes()
        if selected_indexes_cliente:#Conversione listobject to object
            bool1 = False
            selectedCliente = selected_indexes_cliente[0].row()
            cliente = self.controlloreClienti.getCF(lista[selectedCliente])
        selected_indexes_abbonamento = self.listViewAbbonamenti.selectedIndexes()
        if selected_indexes_abbonamento:#Conversione listobject to object
            bool2 = False
            selectedAbb = selected_indexes_abbonamento[0].row()
            abbonamento_selezionato = self.controlloreAbbonamento.get_abbonamenti_by_index(selectedAbb)
            abbonamento = self.controlloreAbbonamento.getTipo(abbonamento_selezionato)
            dataInizio = datetime.date.today()
            dataFine = dataInizio + datetime.timedelta(days=int(self.controlloreAbbonamento.getDurata(abbonamento_selezionato)))
        id = "_" + str(self.controller.id_chooser())
        if bool1 or bool2:
            msg = QMessageBox(
                text="Errore!",
                parent=None)
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setInformativeText("")
            msg.setWindowTitle("Errore!")
            msg.exec()
        else:
            self.controller.aggiungi_iscrizioni(Iscrizioni
                                                ((cliente+id).lower(),
                                                 cliente,
                                                 abbonamento,
                                                 dataFine,
                                                 dataInizio))
            self.controlloreClienti.setIscrizione(lista[selectedCliente], cliente+id)
        self.callback()
        self.close()