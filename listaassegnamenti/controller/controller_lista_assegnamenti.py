from listaassegnamenti.model.lista_assegnamenti import ListaAssegnamenti
class ControllerListaAssegnamenti():
    def __init__(self):
        self.model = ListaAssegnamenti()
    def aggiungi_assegnamenti(self, Assegnamenti):
        self.model.aggiungi_assegnamenti(Assegnamenti)
        self.save_data()
    def get_lista_assegnamenti(self):
        return self.model.get_lista_assegnamenti()
    def get_assegnamenti_by_index(self, codice):
        return self.model.get_assegnamenti_by_index(codice)
    def rimuovi_assegnamenti_by_index(self, codice):
        self.model.rimuovi_assegnamenti_by_index(codice)
        self.save_data()

    def getCodice(self, assegnammenti):
        return self.model.getCodice(assegnammenti)
    def getPrenotazione(self,assegnamenti):
        return assegnamenti.prenotazione
    def getCliente(self, assegnammenti):
        return self.model.getCliente(assegnammenti)
    def getPrenotazioni(self, assegnammenti):
        return self.model.getPrenotazioni(assegnammenti)
    def getServizio(self, assegnammenti):
        return self.model.getServizio(assegnammenti)
    def ricercaAssegnamento(self, codice):
        self.lista_assegnamenti_ricercata = []
        for assegnamenti in self.get_lista_assegnamenti():
            if codice.lower() in assegnamenti.codice.lower():
                self.lista_assegnamenti_ricercata.append(assegnamenti)
        return self.lista_assegnamenti_ricercata
    def rimuoviAssegnamento(self,codice):
        self.model.rimuoviAssegnamento(codice)
        self.save_data()

    def save_data(self):
        self.model.save_data()
    def id_chooser(self):
        if len(self.get_lista_assegnamenti()) == 0:
            return 1
        for assegnamenti in self.get_lista_assegnamenti():
            compare = assegnamenti.codice.split("_")
        intid = int(compare[1]) + 1
        return intid