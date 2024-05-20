from listaabbonamenti.model.lista_abbonamenti import ListaAbbonamenti
class ControllerListaAbbonamenti():
    def __init__(self):
        self.model = ListaAbbonamenti()
    def aggiungi_abbonamenti(self, Abbonamenti):
        self.model.aggiungi_abbonamenti(Abbonamenti)
        self.save_data()
    def get_lista_abbonamenti(self):
        return self.model.get_lista_abbonamenti()
    def get_abbonamenti_by_index(self, id):
        return self.model.get_abbonamenti_by_index(id)
    def rimuovi_abbonamenti_by_index(self, id):
        self.model.rimuovi_abbonamenti_by_index(id)
        self.save_data()
    def getCodice(self, abbonamento):
        return self.model.getCodice(abbonamento)
    def getCosto(self, abbonamento):
        return self.model.getCosto(abbonamento)
    def getDurata(self, abbonamento):
        return self.model.getDurata(abbonamento)
    def getTipo(self, abbonamento):
        return self.model.getTipo(abbonamento)
    def ricercaAbbonamento(self, codice):
        self.lista_abbonamenti_ricercata = []
        for abbonamenti in self.get_lista_abbonamenti():
            if codice.lower() in abbonamenti.codice.lower():
                self.lista_abbonamenti_ricercata.append(abbonamenti)
        return self.lista_abbonamenti_ricercata
    def rimuoviAbbonamento(self,codice):
        self.model.rimuoviAbbonamento(codice)
        self.save_data()
    def setInfoAbbonamento(self, abbonamento,costo,durata):
        self.model.setInfoAbbonamento(abbonamento,costo,durata)
        self.save_data()
    def save_data(self):
        self.model.save_data()
    def id_chooser(self):
        if len(self.get_lista_abbonamenti()) == 0:
            return 1
        for abbonamenti in self.get_lista_abbonamenti():
            compare = abbonamenti.codice.split("_")
        intid = int(compare[1]) + 1
        return intid