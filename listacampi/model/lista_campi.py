import json
import os.path
import pickle

from obj.Campi import Campi


class ListaCampi():

    def __init__(self):
        self.lista_campi = []
        if os.path.isfile('listacampi/data/lista_campi_salvata.pickle'):
            with open('listacampi/data/lista_campi_salvata.pickle', 'rb') as f:
                self.lista_campi = pickle.load(f)
        else:
            self.lista_campi = []
            os.makedirs('listacampi/data', exist_ok=True)
            with open('listacampi/data/lista_campi_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_campi, f)
    def aggiungi_campi(self, Campi):
        self.lista_campi.append(Campi)

    def getCodice(self, Campo):
        return Campo.codice
    def getdurataTurno(self, Campo):
        return Campo.durataTurno
    def getTipo(self, Campo):
        return Campo.tipo
    def rimuoviCampo(self, codice):
        for Campo in self.lista_campi:
            if Campo.codice == codice:
                self.lista_campi.remove(Campo)
                break

    def get_campi_by_index(self, id):
        return self.lista_campi[id]

    def get_lista_campi(self):
        return self.lista_campi

    def rimuovi_campi_by_index(self, id):
        self.lista_campi.remove(self.lista_campi[id])
    def save_data(self):
        with open('listacampi/data/lista_campi_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_campi, handle, pickle.HIGHEST_PROTOCOL)