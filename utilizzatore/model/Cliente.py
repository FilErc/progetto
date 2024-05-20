from utilizzatore.model.Utilizzatore import Utilizzatore

class Cliente(Utilizzatore):
    def __init__(self, nome, cognome, cf, indirizzo, email, telefono):
        super(Cliente, self).__init__(nome,cognome,cf,indirizzo,email,telefono)
        self.iscrizione = ""
