from listaadmin.model.lista_admin import ListaAdmin
class ControllerListaAdmin():
    def __init__(self):
        self.model = ListaAdmin()
    def aggiungi_admin(self, admin):
        self.model.aggiungi_admin(admin)
        self.save_data()
    def get_lista_admin(self):
        return self.model.get_lista_admin()
    def get_admin_by_index(self, index):
        return self.model.get_admin_by_index(index)
    def rimuoviAdmin(self, cf):
        self.model.rimuoviAdmin(cf)
        self.save_data()
    def get_cf_listaadmin(self, cf):
        is_present = False
        for admin in self.get_lista_admin():
            if cf.lower() == admin.cf.lower():
                is_present = True
                break
        return is_present
    def getNome(self,admin):
        return admin.nome
    def getCognome(self,admin):
        return admin.cognome
    def getCF(self,admin):
        return admin.cf
    def getIndirizzo(self,admin):
        return admin.indirizzo
    def getEmail(self,admin):
        return admin.email
    def getTelefono(self,admin):
        return admin.telefono
    def setInfoAdmin(self,cflogged,email,indirizzo,telefono):
        for admin in self.get_lista_admin():
            if admin.cf == cflogged:
                admin.email = email
                admin.indirizzo = indirizzo
                admin.telefono = telefono
                self.save_data()
    def ricercaAdmin(self, admin):
        if self.contiene_numeri(admin):
            string = admin.replace(" ","")
            lista = self.RicercaAdminCF(string)
        else:
            string = admin.replace(" ","")
            lista = self.RicercaAdminNomeCognome(string)
        return lista
    def RicercaAdminCF(self,string):
        lista = []
        for admin in self.get_lista_admin():
            if string.lower() in admin.cf.lower():
                lista.append(admin)
        return lista
    def RicercaAdminNomeCognome(self,string):
        lista_NomeCognome = []
        for admin in self.get_lista_admin():
            if string.lower() in str(admin.nome).lower() + str(admin.cognome).lower():
                lista_NomeCognome.append(admin)
        return lista_NomeCognome
    def contiene_numeri(self, admin):
        for carattere in admin:
            if carattere.isdigit():
                return True
        return False
    def save_data(self):
        self.model.save_data()