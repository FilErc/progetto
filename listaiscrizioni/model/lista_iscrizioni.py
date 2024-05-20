import json
import os.path
import pickle
from obj.Iscrizioni import Iscrizioni
class ListaIscrizioni():
    def __init__(self):
        self.lista_iscrizioni = []
        if os.path.isfile('listaiscrizioni/data/lista_iscrizioni_salvata.pickle'):
            with open('listaiscrizioni/data/lista_iscrizioni_salvata.pickle', 'rb') as f:
                self.lista_iscrizioni = pickle.load(f)
        else:
            self.lista_iscrizioni = []
            os.makedirs('listaiscrizioni/data', exist_ok=True)
            with open('listaiscrizioni/data/lista_iscrizioni_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_iscrizioni, f)
    def aggiungi_iscrizioni(self, Iscrizioni):
        self.lista_iscrizioni.append(Iscrizioni)
    def getCodice(self, Iscrizione):
        return Iscrizione.codice
    def getCliente(self, Iscrizione):
        return Iscrizione.cliente
    def getAbbonamento(self, Iscrizione):
        return Iscrizione.abbonamento
    def getdataFine(self, Iscrizione):
        return Iscrizione.dataFine
    def getdataInizio(self, Iscrizione):
        return Iscrizione.dataInizio
    def rimuoviIscrizione(self, codice):
        for Iscrizione in self.lista_iscrizioni:
            if Iscrizione.codice == codice:
                self.lista_iscrizioni.remove(Iscrizione)

    def get_iscrizioni_by_index(self, codice):
        return self.lista_iscrizioni[codice]
    def get_lista_iscrizioni(self):
        return self.lista_iscrizioni
    def rimuovi_iscrizioni_by_index(self, indice):
        self.lista_iscrizioni.remove(self.lista_iscrizioni[indice])

    def save_data(self):
        with open('listaiscrizioni/data/lista_iscrizioni_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_iscrizioni, handle, pickle.HIGHEST_PROTOCOL)