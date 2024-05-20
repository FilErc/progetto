import json
import os.path
import pickle
from obj.Assegnamenti import Assegnamenti
class ListaAssegnamenti():
    def __init__(self):
        self.lista_assegnamenti = []
        if os.path.isfile('listaassegnamenti/data/lista_assegnamenti_salvata.pickle'):
            with open('listaassegnamenti/data/lista_assegnamenti_salvata.pickle', 'rb') as f:
                self.lista_assegnamenti = pickle.load(f)
        else:
            self.lista_assegnamenti = []
            os.makedirs('listaassegnamenti/data', exist_ok=True)
            with open('listaassegnamenti/data/lista_assegnamenti_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_assegnamenti, f)

    def aggiungi_assegnamenti(self, Assegnamenti):
        self.lista_assegnamenti.append(Assegnamenti)

    def getCodice(self, Assegnamento):
        return Assegnamento.codice
    def getCliente(self, Assegnamento):
        return Assegnamento.cliente
    def getPrenotazioni(self, Assegnamento):
        return Assegnamento.prenotazioni
    def getServizio(self, Assegnamento):
        return Assegnamento.servizio
    def rimuoviAssegnamento(self, codice):
        for assegnamento in self.lista_assegnamenti:
            if assegnamento.codice == codice:
                self.lista_assegnamenti.remove(assegnamento)
                break
    def get_assegnamenti_by_index(self, codice):
        return self.lista_assegnamenti[codice]
    def get_lista_assegnamenti(self):
        return self.lista_assegnamenti
    def rimuovi_assegnamenti_by_index(self, codice):
        self.lista_assegnamenti.remove(self.lista_assegnamenti[codice])
    def save_data(self):
        with open('listaassegnamenti/data/lista_assegnamenti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_assegnamenti, handle, pickle.HIGHEST_PROTOCOL)