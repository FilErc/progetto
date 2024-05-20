import os
import pickle, json
from utilizzatore.model.Admin import Admin
class ListaAdmin():
    def __init__(self):
        self.lista_admin = []
        if os.path.isfile('listaadmin/data/lista_admin_salvata.pickle'):
            with open('listaadmin/data/lista_admin_salvata.pickle', 'rb') as f:
                self.lista_admin = pickle.load(f)
        else:
            self.lista_admin = []
            os.makedirs('listaamin/data', exist_ok=True)
            with open('listaadmin/data/lista_admin_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_admin, f)
    def aggiungi_admin(self, admin):
        self.lista_admin.append(admin)
    def get_admin_by_index(self, index):
        return self.lista_admin[index]
    def rimuoviAdmin(self,cf):
        for admin in self.lista_admin:
            if admin.cf == cf:
                self.lista_admin.remove(admin)
    def get_lista_admin(self):
        return self.lista_admin
    def save_data(self):
        with open('listaadmin/data/lista_admin_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_admin, handle, pickle.HIGHEST_PROTOCOL)