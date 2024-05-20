from listacampi.model.lista_campi import ListaCampi
from datetime import datetime, timedelta

class ControllerListaCampi():

    def __init__(self):
        self.model = ListaCampi()
    def aggiungi_campi(self, Campi):
        self.model.aggiungi_campi(Campi)
    def CrealistaFinale1(self, selected_indexes_campo, campo):
        lista = self.CreaLista(campo)
        if selected_indexes_campo:
            selectedCampo = selected_indexes_campo[0].row()
            codiceCampoSelezionato = lista[selectedCampo]
            for campi in self.get_lista_campi():
                if codiceCampoSelezionato.codice == campi.codice:
                    campo_selezionato = campi
        lista_finale = self.lista_finale(campo_selezionato)
        return lista_finale, campo_selezionato
    def add_minutes_to_time(self, current_time, minutes_to_add):
        # Convert the input time to a datetime object
        dt_time = datetime.strptime(current_time, "%H:%M")

        # Create a timedelta object representing the number of minutes to add
        delta = timedelta(minutes=int(minutes_to_add))

        # Add the timedelta to the original time
        new_time = dt_time + delta

        # Format and return the new time as a string
        return new_time.strftime("%H:%M")

    def add_minutes_to_time_bool(self, current_time, minutes_to_add, durataTurno):
        # Convert the input time to a datetime object
        dt_time = datetime.strptime(current_time, "%H:%M")

        # Create a timedelta object representing the number of minutes to add
        delta = timedelta(minutes=int(minutes_to_add))

        # Add the timedelta to the original time
        new_time = dt_time + delta
        # Format and return the new time as a string
        if new_time <= datetime.strptime("21:00", '%H:%M') - timedelta(minutes=int(durataTurno) + 15):
            return False
        return True
    def lista_finale(self, campo_selezionato):
        lista_finale = []
        k = True
        i = 0
        while k:
            if i == 0:
                lista_finale.append(
                    "09:00 - " + self.add_minutes_to_time("09:00", str(int(campo_selezionato.durataTurno))))
            else:
                lista_finale.append(self.add_minutes_to_time("09:00", str((
                                                                                  int(campo_selezionato.durataTurno) * i) + 15 * i)) + " - " + self.add_minutes_to_time(
                    "09:00", str((int(campo_selezionato.durataTurno) * (i + 1) + 15 * i))))
            if self.add_minutes_to_time_bool("09:00", str((int(campo_selezionato.durataTurno) * (i + 1) + 15 * i)),
                                             campo_selezionato.durataTurno):
                k = False
            i += 1
        return lista_finale
    def CreaLista(self, campo):
        lista = self.ricercaCampoTipo(campo)
        return lista

    def getCodice(self, Campo):
        return self.model.getCodice(Campo)
    def getdurataTurno(self, Campo):
        return self.model.getdurataTurno(Campo)
    def getTipo(self, Campo):
        return self.model.getTipo(Campo)
    def ricercaCampoTipo(self, tipo):
        self.lista_campi_tipo = []
        for Campo in self.get_lista_campi():
            if tipo.lower() in Campo.tipo.lower():
                self.lista_campi_tipo.append(Campo)
        return self.lista_campi_tipo
    def rimuoviCampo(self,codice):
        self.model.rimuoviCampo(codice)
        self.save_data()
    def get_lista_campi(self):
        return self.model.get_lista_campi()

    def get_campi_by_index(self, id):
        return self.model.get_campi_by_index(id)

    def rimuovi_campi_by_index(self, id):
        self.model.rimuovi_campi_by_index(id)
        self.save_data()


    def save_data(self):
        self.model.save_data()

    def id_chooser(self):
        if len(self.get_lista_campi()) == 0:
            return 1
        for campi in self.get_lista_campi():
            compare = campi.codice.split("_")
        intid = int(compare[1]) + 1
        return intid