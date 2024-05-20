from PyQt6.QtCore import QThread, pyqtSignal
from listaprenotazioni.controller.controller_lista_prenotazioni import ControllerListaPrenotazioni
from listaiscrizioni.controller.controller_lista_iscrizioni import ControllerListaIscrizioni
from listaassegnamenti.controller.controller_lista_assegnamenti import ControllerListaAssegnamenti
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
from listadipendente.controller.controller_lista_dipendente import ControllerListaDipendente
from listaadmin.controller.controller_lista_admin import ControllerListaAdmin
from sistema.Backup import ControlloreBackup
import time, datetime,random

#freeze indica dopo quanto tempo ripetere il loop delle scadenze, il counter serve per fixare il ciclo la seconda volta che lo fa dato che sarà sciuramente in default il tempo in secondi prestabilito, nel primo ciclo(quindi ciclo 0) va calcolato quanti secondi mancano all'orario X(scadenza iscrizioni ogni volta alle ore 00:00) in cui deve essere ripetuto il ciclo
class ScadenzaIscrizione(QThread):
    scadenzaIsc = pyqtSignal()
    def Freeze(self,counter):
        if counter <= 1:
            x = -(-(datetime.datetime(year= datetime.datetime.now().year, month= datetime.datetime.now().month, day= datetime.datetime.now().day, hour=0, minute=0, second=0)-datetime.datetime.now()).total_seconds()-86400)
        else:
            x = 864000
        if x == 0:#HO NOTATO CHE NEL TIME.sleep se la x vale 0 crasha
            return 1
        return x
    def run(self):
        counter = 0
        while True:
            self.scadenzaIsc.emit()
            time.sleep(self.Freeze(counter))
            counter += 1
class ScadenzaPrenotazione(QThread):
    scadenzaPre = pyqtSignal()
    def Freeze(self, counter):
        if counter <= 1:
            x = 0
            while int(datetime.datetime.now().second) + x != 60:
               x = x+1
        else:
            x = 60
        if x == 0:
            return 1
        return x
    def run(self):
        counter = 0
        while True:
            self.scadenzaPre.emit()
            time.sleep(self.Freeze(counter))
            counter += 1
class SetBackup(QThread):
    backup_thread = pyqtSignal()
    def Freeze(self,counter):
        if counter <= 1:
            x = -(-(datetime.datetime(year= datetime.datetime.now().year, month= datetime.datetime.now().month, day= datetime.datetime.now().day, hour=23, minute=30, second=0)-datetime.datetime.now()).total_seconds()-86400)
        else:
            x = 864000
        if x == 0:
            return 1
        return x
    def run(self):
        counter = 0
        while True:
            self.backup_thread.emit()
            time.sleep(self.Freeze(counter))
            counter += 1

class ControlloreSistema():
    def SfondoAnimato(self):
        stringa = "QWidget#widget{border-image: url(home/immagini/sfondo.jpg) 0 0 0 0 stretch stretch;background-repeat: no-repeat; border: 0;}QWidget#VistaHome{background-color: black}"
        return stringa
    def eliminaiscrizione(self):
        iscrizioni_da_rimuovere = []
        self.controllerCliente = ControllerListaClienti()
        self.controllerIscrizioni = ControllerListaIscrizioni()
        for i in self.controllerIscrizioni.get_lista_iscrizioni():
            if str(i.dataFine) <= str(datetime.date.today().strftime("%Y-%m-%d")):
                iscrizioni_da_rimuovere.append(i)
        for iscrizione in iscrizioni_da_rimuovere:
            for cliente in self.controllerCliente.get_lista_clienti():
                if cliente.cf == iscrizione.cliente:
                    self.controllerCliente.setIscrizione(cliente, "")
                    self.controllerIscrizioni.rimuoviIscrizione(iscrizione.codice)
            self.controllerIscrizioni.save_data()
    def eliminaprenotazione(self):
        prenotazioni_da_rimuovere = []
        self.controllerPrenotazione = ControllerListaPrenotazioni()
        self.controllerAssegnamento = ControllerListaAssegnamenti()
        for p in self.controllerPrenotazione.get_lista_prenotazioni():
            if (p.data < str(datetime.date.today().strftime("%Y-%m-%d"))) or (p.data == str(datetime.date.today().strftime("%Y-%m-%d")) and str(p.orario[0]+p.orario[1]+p.orario[2]+p.orario[3]+p.orario[4]) <= datetime.datetime.now().strftime("%H:%M")):
                prenotazioni_da_rimuovere.append(p)
        for prenotazione in prenotazioni_da_rimuovere:
            for assegnamento in self.controllerAssegnamento.get_lista_assegnamenti():
                if prenotazione.assegnamento == assegnamento.codice:
                    self.controllerAssegnamento.rimuoviAssegnamento(assegnamento.codice)
                self.controllerPrenotazione.rimuoviPrenotazione(prenotazione.codice)
        self.controllerPrenotazione.save_data()
        self.controllerAssegnamento.save_data()
    def effettuo_backup(self):
        if str(datetime.datetime.today().strftime("%H:%M")) == "23:30":
            self.ControlloreBackup = ControlloreBackup()
            self.ControlloreBackup.start()
    def ScadenzaIscrizioni(self):
        self.scadenza_thread_iscrizioni = ScadenzaIscrizione()
        self.scadenza_thread_iscrizioni.scadenzaIsc.connect(self.eliminaiscrizione)
        self.scadenza_thread_iscrizioni.start()
    def ScadenzaPrenotazioni(self):
        self.scadenza_thread_prenotazioni = ScadenzaPrenotazione()
        self.scadenza_thread_prenotazioni.scadenzaPre.connect(self.eliminaprenotazione)
        self.scadenza_thread_prenotazioni.start()

    def Backup(self):
        self.scadenza_thread_backup = SetBackup()
        self.scadenza_thread_backup.backup_thread.connect(self.effettuo_backup)
        self.scadenza_thread_backup.start()

    def controlloCF(self, cf):
        self.controllerCliente = ControllerListaClienti()
        self.controllerDipendente = ControllerListaDipendente()
        self.controllerAdmin = ControllerListaAdmin()
        for admin in self.controllerAdmin.get_lista_admin():
            if admin.cf.lower() == cf.lower():
                return False
        for dipendente in self.controllerDipendente.get_lista_dipendente():
            if dipendente.cf.lower() == cf.lower():
                return False
        for cliente in self.controllerCliente.get_lista_clienti():
            if cliente.cf.lower() == cf.lower():
                return False
        return True




