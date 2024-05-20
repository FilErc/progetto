from listadipendente.model.lista_dipendente import ListaDipendente


class ControllerListaDipendente():

    def __init__(self):
        self.model = ListaDipendente()

    def aggiungi_dipendente(self, dipendente):
        self.model.aggiungi_dipendente(dipendente)
        self.save_data()
    def get_lista_dipendente(self):
        return self.model.get_lista_dipendente()

    def get_dipendente_by_index(self, index):
        return self.model.get_dipendente_by_index(index)
    def getNome(self, dipendente):
        return dipendente.nome
    def getCognome(self, dipendente):
        return dipendente.cognome
    def getCF(self, dipendente):
        return dipendente.cf
    def getIndirizzo(self, dipendente):
        return dipendente.indirizzo
    def getEmail(self, dipendente):
        return dipendente.email
    def getTelefono(self, dipendente):
        return dipendente.telefono
    def rimuoviDipendente(self, cf):
        self.model.rimuoviDipendente(cf)
        self.save_data()
    def get_cf_listadipendente(self, cf):
        is_present = False
        for dipendente in self.get_lista_dipendente():
            if cf.lower() == dipendente.cf.lower():
                is_present = True
                break
        return is_present
    def setInfoDipendente(self,cflogged,email,indirizzo,telefono):
        for dipendente in self.get_lista_dipendente():
            if dipendente.cf == cflogged:
                dipendente.email = email
                dipendente.indirizzo = indirizzo
                dipendente.telefono = telefono
                self.save_data()
    def ricercaDipendente(self, dipendente):
        if self.contiene_numeri(dipendente):
            string = dipendente.replace(" ","")
            lista = self.RicercaDipendenteCF(string)
        else:
            string = dipendente.replace(" ","")
            lista = self.RicercaDipendenteNomeCognome(string)
        return lista
    def RicercaDipendenteCF(self,string):
        lista = []
        for dipendente in self.get_lista_dipendente():
            if string.lower() in dipendente.cf.lower():
                lista.append(dipendente)
        return lista
    def RicercaDipendenteNomeCognome(self,string):
        lista_NomeCognome = []
        for dipendente in self.get_lista_dipendente():
            if string.lower() in str(dipendente.nome).lower() + str(dipendente.cognome).lower():
                lista_NomeCognome.append(dipendente)
        return lista_NomeCognome
    def contiene_numeri(self, dipendente):
        for carattere in dipendente:
            if carattere.isdigit():
                return True
        return False
    def save_data(self):
        self.model.save_data()