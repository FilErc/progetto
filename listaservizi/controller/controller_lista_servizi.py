from listaservizi.model.lista_servizi import ListaServizi


class ControllerListaServizi():

    def __init__(self):
        self.model = ListaServizi()

    def aggiungi_servizio(self, Servizio):
        self.model.aggiungi_servizio(Servizio)
        self.save_data()
    def get_lista_servizi(self):
        return self.model.get_lista_servizi()
    def get_servizio_by_index(self, id):
        return self.model.get_servizio_by_index(id)

    def rimuoviServizio(self, codice):
        self.model.rimuoviServizio(codice)
        self.save_data()

    def bottoneRicercaServizi(self, Servizi):
        lista = self.ricercaServizioTipo(Servizi)
        return lista
    def getCodice(self, Servizio):
        return self.model.getCodice(Servizio)
    def getTipo(self, Servizio):
        return self.model.getTipo(Servizio)

    def ricercaServizioTipo(self,tipo):
        lista = []
        for Servizio in self.get_lista_servizi():
            if tipo.lower() in Servizio.tipo.lower():
                lista.append(Servizio)
        return lista
    def save_data(self):
        self.model.save_data()

    def id_chooser(self):
        if len(self.get_lista_servizi()) == 0:
            return 1
        for servizio in self.get_lista_servizi():
            compare = servizio.codice.split("_")
        intid = int(compare[1]) + 1
        return intid