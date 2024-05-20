from listaclienti.model.lista_clienti import ListaClienti
from datetime import timedelta, datetime
import time
class ControllerListaClienti():

    def __init__(self):
        self.model = ListaClienti()

    def save_data(self):
        self.model.save_data()
    def getNome(self,cliente):
        return cliente.nome
    def getCognome(self,cliente):
        return cliente.cognome
    def getCF(self,cliente):
        return cliente.cf
    def getIndirizzo(self,cliente):
        return cliente.indirizzo
    def getEmail(self,cliente):
        return cliente.email
    def getTelefono(self,cliente):
        return cliente.telefono
    def getIscrizione(self,cliente):
        return cliente.iscrizione
    def bottoneRicercaCliente(self, cliente):
        if self.contiene_numeri(cliente):
            string = cliente.replace(" ","")
            lista = self.RicercaClienteCF(string)
        else:
            string = cliente.replace(" ","")
            lista = self.RicercaClienteNomeCognome(string)
        return lista
    def contiene_numeri(self, cliente):
        for carattere in cliente:
            if carattere.isdigit():
                return True
        return False
    def create_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente)
        self.save_data()
    def get_lista_clienti(self):
        return self.model.get_lista_clienti()

    def get_cliente_by_index(self, index):
        return self.model.get_cliente_by_index(index)

    def rimuoviCliente(self, cf):
        self.model.rimuoviCliente(cf)
        self.save_data()
    def RicercaClienteCF(self,string):
        lista = []
        for cliente in self.get_lista_clienti():
            if string.lower() in cliente.cf.lower():
                lista.append(cliente)
        return lista
    def RicercaClienteNomeCognome(self,string):
        lista_NomeCognome = []
        for cliente in self.get_lista_clienti():
            if string.lower() in str(cliente.nome).lower() + str(cliente.cognome).lower():
                lista_NomeCognome.append(cliente)
        return lista_NomeCognome
    def getCF(self, cliente):
        return self.model.getCF(cliente)
    def setIscrizione(self, cliente, codiceiscrizione):
        for c in self.get_lista_clienti():
            if c.cf.lower() == cliente.cf.lower():
                c.iscrizione = codiceiscrizione
        self.save_data()
    def setInfoCliente(self,cflogged,email,indirizzo,telefono):
        for Cliente in self.get_lista_clienti():
            if Cliente.cf == cflogged:
                Cliente.email = email
                Cliente.indirizzo = indirizzo
                Cliente.telefono = telefono
                self.save_data()
    def get_cf_listacliente(self, cf):
        is_present = False
        for cliente in self.get_lista_clienti():
            if cf.lower() == cliente.cf.lower():
                is_present = True
                break
        return is_present
