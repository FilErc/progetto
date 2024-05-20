from listaprenotazioni.model.lista_prenotazioni import ListaPrenotazioni


class ControllerListaPrenotazioni():

    def __init__(self):
        self.model = ListaPrenotazioni()

    def aggiungi_prenotazione(self, Prenotazione):
        self.model.aggiungi_prenotazione(Prenotazione)
        self.save_data()
    def CreaListaFinale2(self, lista_finale, campo_selezionato, data_selezionata):
        for prenotazione in self.get_lista_prenotazioni():
            if data_selezionata == prenotazione.data:
                if campo_selezionato.codice == prenotazione.campo:
                    for j in lista_finale:
                        if prenotazione.orario == j:
                            lista_finale.remove(j)
        return lista_finale
    def get_lista_prenotazioni(self):
        return self.model.get_lista_prenotazioni()

    def get_prenotazione_by_index(self, id):
        return self.model.get_prenotazione_by_index(id)

    def rimuovi_prenotazione_by_index(self, id):
        self.model.rimuovi_prenotazione_by_index(id)
        self.save_data()

    def bottoneRicercaPrenotazioni(self, Prenotazioni):
        lista = self.ricercaPrenotazione(Prenotazioni)
        return lista

    def getCodice(self, Prenotazione):
        return self.model.getCodice(Prenotazione)
    def getCampo(self, Prenotazione):
        return self.model.getCampo(Prenotazione)
    def getCliente(self, Prenotazione):
        return self.model.getCliente(Prenotazione)
    def getAssegnamento(self, Prenotazione):
        return self.model.getAssegnamento(Prenotazione)
    def getData(self, Prenotazione):
        return str(self.model.getData(Prenotazione))
    def getOrario(self, Prenotazione):
        return self.model.getOrario(Prenotazione)
    def ricercaPrenotazione(self, codice):
        self.lista_prenotazioni_ricercata = []
        for Prenotazione in self.get_lista_prenotazioni():
            if codice.lower() in Prenotazione.codice.lower():
                self.lista_prenotazioni_ricercata.append(Prenotazione)
        return self.lista_prenotazioni_ricercata
    def rimuoviPrenotazione(self,codice):
        self.model.rimuoviPrenotazione(codice)
        self.save_data()
    def setAssegnamento(self, Prenotazione, assegnamento):
        self.model.setAssegnamento(Prenotazione, assegnamento)
        self.save_data()

    def save_data(self):
        self.model.save_data()

    def id_chooser(self):
        if len(self.get_lista_prenotazioni()) == 0:
            return 1
        for prenotazione in self.get_lista_prenotazioni():
            compare = prenotazione.codice.split("_")
        intid = int(compare[1]) + 1
        return intid