import json
import os.path
import pickle

from obj.Servizio import Servizio


class ListaServizi():

    def __init__(self):
        self.lista_servizi = []
        if os.path.isfile('listaservizi/data/lista_servizi_salvata.pickle'):
            with open('listaservizi/data/lista_servizi_salvata.pickle', 'rb') as f:
                self.lista_servizi = pickle.load(f)
        else:
            self.lista_servizi = []
            os.makedirs('listaservizi/data', exist_ok=True)
            with open('listaservizi/data/lista_servizi_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_servizi, f)
    def aggiungi_servizio(self, Servizio):
        self.lista_servizi.append(Servizio)

    def getCodice(self, Servizio):
        return Servizio.codice

    def getTipo(self, Servizio):
        return Servizio.tipo
    def rimuoviServizio(self, codice):
        for Servizio in self.lista_servizi:
            if Servizio.codice == codice:
                self.lista_servizi.remove(Servizio)
                break
    def get_servizio_by_index(self, id):
        return self.lista_servizi[id]

    def get_lista_servizi(self):
        return self.lista_servizi

    def rimuoviServizio(self, id):
        self.lista_servizi.remove(self.lista_servizi[id])
    def save_data(self):
        with open('listaservizi/data/lista_servizi_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_servizi, handle, pickle.HIGHEST_PROTOCOL)