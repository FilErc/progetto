from listaiscrizioni.model.lista_iscrizioni import ListaIscrizioni
from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
class ControllerListaIscrizioni():
    def __init__(self):
        self.model = ListaIscrizioni()
    def aggiungi_iscrizioni(self, Iscrizioni):
        self.model.aggiungi_iscrizioni(Iscrizioni)
        self.save_data()
    def get_lista_iscrizioni(self):
        return self.model.get_lista_iscrizioni()
    def get_iscrizioni_by_index(self, codice):
        return self.model.get_iscrizioni_by_index(codice)
    def rimuovi_iscrizioni_by_index(self, indice):
        self.controller = ControllerListaClienti()
        listaIscrizioni = self.get_lista_iscrizioni()
        for cliente in self.controller.get_lista_clienti():
            if (cliente.iscrizione is not None and cliente.iscrizione.lower() == listaIscrizioni[indice].codice):
                self.controller.setIscrizione(cliente, "")
        self.model.rimuovi_iscrizioni_by_index(indice)
        self.save_data()
    def getCodice(self, iscrizione):
        return self.model.getCodice(iscrizione)
    def getCliente(self, iscrizione):
        return self.model.getCliente(iscrizione)
    def getAbbonamento(self, iscrizione):
        return self.model.getAbbonamento(iscrizione)
    def getdataFine(self, iscrizione):
        return str(self.model.getdataFine(iscrizione))
    def getdataInizio(self, iscrizione):
        return str(self.model.getdataInizio(iscrizione))

    def ricercaIscrizione(self, codice):
        self.lista_iscrizione_ricercata = []
        for iscrizione in self.get_lista_iscrizioni():
            if codice.lower() in iscrizione.codice.lower():
                self.lista_iscrizione_ricercata.append(iscrizione)
        return self.lista_iscrizione_ricercata
    def rimuoviIscrizione(self,codice):
        self.model.rimuoviIscrizione(codice)
        self.save_data()

    def save_data(self):
        self.model.save_data()

    def id_chooser(self):
        if len(self.get_lista_iscrizioni()) == 0:
            return 1
        for iscrizioni in self.get_lista_iscrizioni():
            compare = iscrizioni.codice.split("_")
        intid = int(compare[1]) + 1
        return intid