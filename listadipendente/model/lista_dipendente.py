import os
import pickle, json

from utilizzatore.model.Dipendente import Dipendente
class ListaDipendente():
    def __init__(self):
        self.lista_dipendente = []
        if os.path.isfile('listadipendente/data/lista_dipendente_salvata.pickle'):
            with open('listadipendente/data/lista_dipendente_salvata.pickle', 'rb') as f:
                self.lista_dipendente = pickle.load(f)
        else:
            self.lista_dipendente = []
            os.makedirs('listadipendente/data', exist_ok=True)
            with open('listadipendente/data/lista_dipendente_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_dipendente, f)

    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendente.append(dipendente)
    def rimuoviDipendente(self, cf):
        for d in self.lista_dipendente:
            if d.cf == cf:
                self.lista_dipendente.remove(d)

    def get_dipendente_by_index(self, index):
        return self.lista_dipendente[index]

    def get_lista_dipendente(self):
        return self.lista_dipendente



    def save_data(self):
        with open('listadipendente/data/lista_dipendente_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_dipendente, handle, pickle.HIGHEST_PROTOCOL)