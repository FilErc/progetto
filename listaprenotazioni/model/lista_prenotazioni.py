import json
import os.path
import pickle

from obj.Prenotazione import Prenotazione


class ListaPrenotazioni():

    def __init__(self):
        self.lista_prenotazioni = []
        if os.path.isfile('listaprenotazioni/data/lista_prenotazioni_salvata.pickle'):
            with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'rb') as f:
                self.lista_prenotazioni = pickle.load(f)
        else:
            self.lista_prenotazioni = []
            os.makedirs('listaprenotazioni/data', exist_ok=True)
            with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_prenotazioni, f)

    def aggiungi_prenotazione(self, Prenotazione):
        self.lista_prenotazioni.append(Prenotazione)
    def getCodice(self, Prenotazione):
        return Prenotazione.codice
    def getCampo(self, Prenotazione):
        return Prenotazione.campo
    def getCliente(self, Prenotazione):
        return Prenotazione.cliente
    def getAssegnamento(self, Prenotazione):
        return Prenotazione.assegnamento
    def getData(self, Prenotazione):
        return Prenotazione.data
    def getOrario(self, Prenotazione):
        return Prenotazione.orario
    def rimuoviPrenotazione(self, codice):
        for Prenotazione in self.lista_prenotazioni:
            if Prenotazione.codice == codice:
                self.lista_prenotazioni.remove(Prenotazione)
                break
    def setAssegnamento(self,Prenotazione, assegnamento):
        Prenotazione.assegnamento = assegnamento

    def get_prenotazione_by_index(self, id):
        return self.lista_prenotazioni[id]

    def get_lista_prenotazioni(self):
        return self.lista_prenotazioni

    def rimuovi_prenotazione_by_index(self, id):
        self.lista_prenotazioni.remove(self.lista_prenotazioni[id])

    def save_data(self):
        with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_prenotazioni, handle, pickle.HIGHEST_PROTOCOL)