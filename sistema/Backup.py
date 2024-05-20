from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
from listadipendente.controller.controller_lista_dipendente import ControllerListaDipendente
from listaadmin.controller.controller_lista_admin import ControllerListaAdmin
from listaabbonamenti.controller.controller_lista_abbonamenti import ControllerListaAbbonamenti
from listaassegnamenti.controller.controller_lista_assegnamenti import ControllerListaAssegnamenti
from listacampi.controller.controller_lista_campi import ControllerListaCampi
from listaiscrizioni.controller.controller_lista_iscrizioni import ControllerListaIscrizioni
from listaprenotazioni.controller.controller_lista_prenotazioni import ControllerListaPrenotazioni
from listaservizi.controller.controller_lista_servizi import ControllerListaServizi
import os, pickle, datetime
class ControlloreBackup():
    if not os.path.exists("Backup"):#QUESTA PARTE DI CODICE VIENE LETTA NEL LOGIC NON SO IL PERCHE'
        os.makedirs("Backup")
    def start(self):
        self.controlloreClienti = ControllerListaClienti()
        self.controlloreDipendenti = ControllerListaDipendente()
        self.controlloreAdmin = ControllerListaAdmin()
        self.controlloreAbbonamenti = ControllerListaAbbonamenti()
        self.controlloreAssegnamenti = ControllerListaAssegnamenti()
        self.controlloreCampi = ControllerListaCampi()
        self.controlloreIscrizioni = ControllerListaIscrizioni()
        self.controllorePrenotazioni = ControllerListaPrenotazioni()
        self.controlloreServizi = ControllerListaServizi()
        os.makedirs("Backup/"+str(datetime.date.today().strftime("%Y-%d-%m")))
        with open ("Backup/"+str(datetime.date.today().strftime("%Y-%d-%m"))+"/"+"ClientiBackup.pickle","wb") as file:
                pickle.dump(self.controlloreClienti.get_lista_clienti(), file)
        with open("Backup/"+str(datetime.date.today().strftime("%Y-%d-%m"))+"/"+"DipendentiBackup.pickle", 'wb') as file:
            pickle.dump(self.controlloreDipendenti.get_lista_dipendente(), file)
        with open("Backup/"+str(datetime.date.today().strftime("%Y-%d-%m"))+"/"+"AdminBackup.pickle", 'wb') as file:
            pickle.dump(self.controlloreAdmin.get_lista_admin(), file)
        with open("Backup/"+str(datetime.date.today().strftime("%Y-%d-%m"))+"/"+"AbbonamentiBackup.pickle", 'wb') as file:
            pickle.dump(self.controlloreAbbonamenti.get_lista_abbonamenti(), file)
        with open("Backup/"+str(datetime.date.today().strftime("%Y-%d-%m"))+"/"+"AssegnamentiBackup.pickle", 'wb') as file:
            pickle.dump(self.controlloreAssegnamenti.get_lista_assegnamenti(), file)
        with open("Backup/"+str(datetime.date.today().strftime("%Y-%d-%m"))+"/"+"CampiBackup.pickle", 'wb') as file:
            pickle.dump(self.controlloreCampi.get_lista_campi(), file)
        with open("Backup/"+str(datetime.date.today().strftime("%Y-%d-%m"))+"/"+"IscrizioniBackup.pickle", 'wb') as file:
            pickle.dump(self.controlloreIscrizioni.get_lista_iscrizioni(), file)
        with open("Backup/"+str(datetime.date.today().strftime("%Y-%d-%m"))+"/"+"PrenotazioniBackup.pickle", 'wb') as file:
            pickle.dump(self.controllorePrenotazioni.get_lista_prenotazioni(), file)
        with open("Backup/"+str(datetime.date.today().strftime("%Y-%d-%m"))+"/"+"ServiziBackup.pickle", 'wb') as file:
            pickle.dump(self.controlloreServizi.get_lista_servizi(), file)

