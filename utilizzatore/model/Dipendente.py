from utilizzatore.model.Utilizzatore import Utilizzatore

class Dipendente(Utilizzatore):
    def __init__(self, nome, cognome, cf, indirizzo, email,
                 telefono):
        super(Dipendente, self).__init__(nome, cognome, cf, indirizzo, email, telefono,)