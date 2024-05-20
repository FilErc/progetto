import json
import os.path
import pickle

class ListaAbbonamenti():
    def __init__(self):
        self.lista_abbonamenti = []
        if os.path.isfile('listaabbonamenti/data/lista_abbonamenti_salvata.pickle'):
            with open('listaabbonamenti/data/lista_abbonamenti_salvata.pickle', 'rb') as f:
                self.lista_abbonamenti = pickle.load(f)
        else:
            self.lista_abbonamenti = []
            os.makedirs('listaabbonamenti/data', exist_ok=True)
            with open('listaabbonamenti/data/lista_abbonamenti_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_abbonamenti, f)


    def aggiungi_abbonamenti(self, Abbonamenti):
        self.lista_abbonamenti.append(Abbonamenti)
    def getCodice(self, Abbonamento):
        return Abbonamento.codice
    def getCosto(self, Abbonamento):
        return Abbonamento.costo
    def getDurata(self, Abbonamento):
        return Abbonamento.durata
    def getTipo(self, Abbonamento):
        return Abbonamento.tipo

    def rimuoviAbbonamento(self, codice):
        for abbonamento in self.lista_abbonamenti:
            if abbonamento.codice == codice:
                self.lista_abbonamenti.remove(abbonamento)
    def setInfoAbbonamento(self,abbonamento, costo, durata):
        abbonamento.costo = costo
        abbonamento.durata = durata
    def visualizzaAbbonamento(self, codice):
        for Abbonamento in self.lista_abbonamenti:
            if Abbonamento.codice == codice:
                return str(Abbonamento.codice) + "-" + str(Abbonamento.costo) + "-" + str(Abbonamento.durata) + "-" + str(Abbonamento.tipo)
    def get_abbonamenti_by_index(self, id):#funzione non presente nella classe di progettazione
        return self.lista_abbonamenti[id]
    def get_lista_abbonamenti(self):#funzione non presente nella classe di progettazione
        return self.lista_abbonamenti
    def rimuovi_abbonamenti_by_index(self, id):#id=INDICE non CODICE
        self.lista_abbonamenti.remove(self.lista_abbonamenti[id])
    def save_data(self):
        with open('listaabbonamenti/data/lista_abbonamenti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_abbonamenti, handle, pickle.HIGHEST_PROTOCOL)