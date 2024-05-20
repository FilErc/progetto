from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
from listadipendente.controller.controller_lista_dipendente import ControllerListaDipendente
from listaadmin.controller.controller_lista_admin import ControllerListaAdmin
from listaabbonamenti.controller.controller_lista_abbonamenti import ControllerListaAbbonamenti
from listaassegnamenti.controller.controller_lista_assegnamenti import ControllerListaAssegnamenti
from listacampi.controller.controller_lista_campi import ControllerListaCampi
from listaiscrizioni.controller.controller_lista_iscrizioni import ControllerListaIscrizioni
from listaprenotazioni.controller.controller_lista_prenotazioni import ControllerListaPrenotazioni
from listaservizi.controller.controller_lista_servizi import ControllerListaServizi

class GestoreStatistiche():
    #LEN ritorna un intero quindi va fatto -1 per togliere il default
    def NumeroClienti(self):
        self.controlloreClienti = ControllerListaClienti()
        return len(self.controlloreClienti.get_lista_clienti())
    def NumeroDipendenti(self):
        self.controlloreDipendenti = ControllerListaDipendente()
        return len(self.controlloreDipendenti.get_lista_dipendente())
    def NumeroAdmin(self):
        self.controlloreAdmin = ControllerListaAdmin()
        return len(self.controlloreAdmin.get_lista_admin())
    def NumeroAbbonamenti(self):
        self.controlloreAbbonamenti = ControllerListaAbbonamenti()
        return len(self.controlloreAbbonamenti.get_lista_abbonamenti())
    def NumeroAssegnamenti(self):
        self.controlloreAssegnamenti = ControllerListaAssegnamenti()
        return len(self.controlloreAssegnamenti.get_lista_assegnamenti())
    def NumeroCampi(self):
        self.controlloreCampi = ControllerListaCampi()
        return len(self.controlloreCampi.get_lista_campi())
    def NumeroIscrizioni(self):
        self.controlloreIscrizioni = ControllerListaIscrizioni()
        return len(self.controlloreIscrizioni.get_lista_iscrizioni())
    def NumeroPrenotazioni(self):
        self.controllorePrenotazioni = ControllerListaPrenotazioni()
        return len(self.controllorePrenotazioni.get_lista_prenotazioni())
    def NumeroServizi(self):
        self.controlloreServizi = ControllerListaServizi()
        return len(self.controlloreServizi.get_lista_servizi())
    def ClassificaCampiScelti(self):
        self.controllorePrenotazioni = ControllerListaPrenotazioni()
        Classifica = {}
        for prenotazione in self.controllorePrenotazioni.get_lista_prenotazioni():
            campo = prenotazione.campo.split("_")
            if campo[0] != "default":
                if campo[0] in Classifica:
                    Classifica[campo[0]] += 1
                else:
                    Classifica[campo[0]] = 1
        Classifica_ordinata = sorted(Classifica.items(), key=lambda x: x[1], reverse=True)
        classifica_stringa = ""
        for campo, conteggio in Classifica_ordinata:
            classifica_stringa += f"{campo}: {conteggio} volte\n"
        return classifica_stringa
    def ClassificaServiziScelti(self):
        self.controlloreAssegnamenti = ControllerListaAssegnamenti()
        Classifica = {}
        for assegnamento in self.controlloreAssegnamenti.get_lista_assegnamenti():
            servizio = assegnamento.servizio.split("_")
            if servizio[0] != "default":
                if servizio[0] in Classifica:
                    Classifica[servizio[0]] += 1
                else:
                    Classifica[servizio[0]] = 1
        Classifica_ordinata = sorted(Classifica.items(), key=lambda x: x[1], reverse=True)
        classifica_stringa = ""
        for servizio, conteggio in Classifica_ordinata:
            classifica_stringa += f"{servizio}: {conteggio} volte\n"
        return classifica_stringa
    def ClassificaAbbonamentiScelti(self):
        self.controlloreIscrizioni = ControllerListaIscrizioni()
        Classifica = {}
        for iscrizioni in self.controlloreIscrizioni.get_lista_iscrizioni():
            abbonamento = iscrizioni.abbonamento.split("_")
            if abbonamento[0] != "default":
                if abbonamento[0] in Classifica:
                    Classifica[abbonamento[0]] += 1
                else:
                    Classifica[abbonamento[0]] = 1
        Classifica_ordinata = sorted(Classifica.items(), key=lambda x: x[1], reverse=True)
        classifica_stringa = ""
        for abbonamento, conteggio in Classifica_ordinata:
            classifica_stringa += f"{abbonamento}: {conteggio} volte\n"
        return classifica_stringa

