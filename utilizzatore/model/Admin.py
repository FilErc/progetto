from utilizzatore.model.Utilizzatore import Utilizzatore

class Admin(Utilizzatore):
    def __init__(self, nome, cognome, cf, indirizzo, email, telefono):
        super(Admin, self).__init__(nome, cognome, cf, indirizzo, email, telefono)