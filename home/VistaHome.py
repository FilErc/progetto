import datetime

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QProgressBar, QLineEdit, QMessageBox
from PyQt6 import uic
from listaclienti.view.vista_lista_clienti import VistaListaClienti
from listaservizi.view.vista_lista_servizi import VistaListaServizi
from listacampi.view.vista_lista_campi import VistaListaCampi
from listadipendente.view.vista_lista_dipendente import VistaListaDipendente
from listaadmin.view.vista_lista_admin import VistaListaAdmin
from listaabbonamenti.view.vista_lista_abbonamenti import VistaListaAbbonamenti
from listaprenotazioni.view.vista_lista_prenotazioni import VistaListaPrenotazioni
from listaassegnamenti.view.vista_lista_assegnamenti import VistaListaAssegnamenti
from listaiscrizioni.view.vista_lista_iscrizioni import VistaListaIscrizioni
from utilizzatore.view.vista_lista_statistiche import VistaListaStatistiche
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
from listadipendente.controller.controller_lista_dipendente import ControllerListaDipendente
from listaadmin.controller.controller_lista_admin import ControllerListaAdmin
from sistema.Sistema import ControlloreSistema
from listaassegnamenti.controller.controller_lista_assegnamenti import ControllerListaAssegnamenti
from sistema.Statistiche import GestoreStatistiche
from listaprenotazioni.controller.controller_lista_prenotazioni import ControllerListaPrenotazioni
from listacampi.controller.controller_lista_campi import ControllerListaCampi

class VistaHome(QWidget):
    def __init__(self, cflogged, parent=None):
        super(VistaHome, self).__init__(parent)
        self.controllerSistema = ControlloreSistema()
        self.controllerSistema.ScadenzaIscrizioni()
        self.controllerSistema.ScadenzaPrenotazioni()
        self.controllerSistema.Backup()
        HomeCliente = False
        HomeDipendente = False
        HomeAdmin = False
        self.controller = ControllerListaClienti()
        for cliente in self.controller.get_lista_clienti():
            if cliente.cf.lower() == cflogged.lower():
                HomeCliente = True
                break
        if not HomeCliente:
            self.controller = ControllerListaDipendente()
            for dipendente in self.controller.get_lista_dipendente():
                if dipendente.cf.lower() == cflogged.lower():
                    HomeDipendente = True
                    break
        if not HomeCliente and not HomeDipendente:
            self.controller = ControllerListaAdmin()
            for admin in self.controller.get_lista_admin():
                if admin.cf.lower() == cflogged.lower():
                    HomeAdmin = True
        if HomeAdmin:
            uic.loadUi('home/vistahome_admin.ui', self)
        elif HomeDipendente:
            uic.loadUi("home/vistahome_dipendente.ui", self)
        elif HomeCliente:
            uic.loadUi("home/vistahome_cliente.ui", self)
            self.controllerPre = ControllerListaPrenotazioni()
            self.update_ui(cflogged)
            self.labelNomeCognome.setText(f"{self.controller.getNome(cliente)} {self.controller.getCognome(cliente)}")
            self.labelNomeCognome.setReadOnly(True)
            self.labelCF.setText(f"{self.controller.getCF(cliente)}")
            self.labelCF.setReadOnly(True)
            self.labelEmail.setText(f"{self.controller.getEmail(cliente)}")
            self.labelEmail.setReadOnly(True)
            self.labelIndirizzo.setText(f"{self.controller.getIndirizzo(cliente)}")
            self.labelIndirizzo.setReadOnly(True)
            self.labelTelefono.setText(f"{self.controller.getTelefono(cliente)}")
            self.labelTelefono.setReadOnly(True)
            self.labelAbbonamento.setText(f"{self.controller.getIscrizione(cliente)}")
            self.labelAbbonamento.setReadOnly(True)
        self.setStyleSheet("QWidget#widget{border-image: url(home/immagini/sfondo.jpg) 0 0 0 0 stretch stretch;background-repeat: no-repeat; border: 0;}QWidget#VistaHome{background-color: black}")
        self.showMaximized()
        self.cf = cflogged
        if HomeAdmin:
            self.servizi_button_2.clicked.connect(self.go_lista_servizi)
        if HomeAdmin or HomeDipendente:
            self.clienti_button_2.clicked.connect(self.go_lista_clienti)
        if HomeAdmin:
            self.campo_button_2.clicked.connect(self.go_lista_campi)
        if HomeAdmin:
            self.staff_button_2.clicked.connect(self.go_lista_staff)
        if HomeAdmin:
            self.abbonamento_button_2.clicked.connect(self.go_lista_abbonamenti)
        if HomeAdmin or HomeDipendente:
            self.prenotazioni_button_2.clicked.connect(lambda: self.go_lista_prenotazioni(HomeDipendente))
        if HomeAdmin:
            self.admin_button_2.clicked.connect(self.go_lista_admin)
        if HomeAdmin or HomeDipendente:
            self.assegnamento_button_2.clicked.connect(self.go_lista_assegnamenti)
        if HomeAdmin or HomeDipendente:
            self.iscrizioni_button_2.clicked.connect(self.go_lista_iscrizioni)
        if HomeAdmin:
            self.statistiche_button_2.clicked.connect(self.go_lista_statistiche)
        if HomeCliente:
            self.pushButton_2.clicked.connect(lambda: self.go_disdetta(cflogged))
    def update_ui(self,cflogged):
        self.listview_model = QStandardItemModel(self.listViewPrenotazioni)
        for prenotazione in self.controllerPre.ricercaPrenotazione(cflogged):
            item = QStandardItem()
            campo = prenotazione.campo.split("_")
            item.setText(f"{prenotazione.data} | {prenotazione.orario} | {campo[0]}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listViewPrenotazioni.setModel(self.listview_model)
    def go_disdetta(self,cflogged):
        selected_indexes = self.listViewPrenotazioni.selectedIndexes()
        if selected_indexes:
            self.controlloreAssegnamenti = ControllerListaAssegnamenti()
            selected = selected_indexes[0].row()
            prenotazione = self.controllerPre.get_prenotazione_by_index(selected)
            if str(datetime.date.today()+datetime.timedelta(days=6)) < str(prenotazione.data):
                for p in self.controllerPre.get_lista_prenotazioni():
                    if p.codice == prenotazione.codice:
                        self.controlloreAssegnamenti.rimuoviAssegnamento(prenotazione.assegnamento)
                self.controllerPre.rimuoviPrenotazione(prenotazione.codice)
            else:
                msg = QMessageBox(
                    text="Errore!",
                    parent=self)
                msg.setIcon(QMessageBox.Icon.Question)
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.setInformativeText("")
                msg.exec()
        self.update_ui(cflogged)

    def go_lista_servizi(self):
        self.vista_lista_servizi = VistaListaServizi()
        self.vista_lista_servizi.show()
    def go_lista_clienti(self):
        self.vista_lista_clienti = VistaListaClienti()
        self.vista_lista_clienti.show()
    def go_lista_campi(self):
        self.vista_lista_campi = VistaListaCampi()
        self.vista_lista_campi.show()
    def go_lista_staff(self):
        self.vista_lista_staff = VistaListaDipendente()
        self.vista_lista_staff.show()
    def go_lista_abbonamenti(self):
        self.vista_lista_abbonamenti = VistaListaAbbonamenti()
        self.vista_lista_abbonamenti.show()
    def go_lista_admin(self):
        self.vista_lista_admin = VistaListaAdmin()
        self.vista_lista_admin.show()
    def go_lista_prenotazioni(self, HomeDipendente):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni(HomeDipendente)
        self.vista_lista_prenotazioni.show()
    def go_lista_assegnamenti(self):
        self.vista_lista_assegnamenti = VistaListaAssegnamenti()
        self.vista_lista_assegnamenti.show()
    def go_lista_iscrizioni(self):
        self.vista_lista_iscrizioni = VistaListaIscrizioni()
        self.vista_lista_iscrizioni.show()
    def go_lista_statistiche(self):
        self.vista_lista_statistiche = VistaListaStatistiche()
        self.vista_lista_statistiche.show()