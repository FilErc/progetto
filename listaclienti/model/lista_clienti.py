import os
import pickle, json

from utilizzatore.model.Cliente import Cliente

class ListaClienti():
    def __init__(self):
        self.lista_clienti = []
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)
        else:
            self.lista_clienti = []
            os.makedirs('listaclienti/data', exist_ok=True)
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_clienti, f)

    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)

    def getCF(self,cliente):
        return cliente.cf
    def get_cliente_by_index(self, index):
        return self.lista_clienti[index]
    def rimuoviCliente(self,cf):
        for c in self.lista_clienti:
            if c.cf == cf:
                self.lista_clienti.remove(c)

    def get_lista_clienti(self):
        return self.lista_clienti

    def save_data(self):
        with open('listaclienti/data/lista_clienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)
