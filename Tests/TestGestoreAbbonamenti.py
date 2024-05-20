import datetime
import os
import pickle
import unittest
from listaabbonamenti.controller.controller_lista_abbonamenti import ControllerListaAbbonamenti
from obj.Abbonamenti import Abbonamenti


class TestGestoreAbbonamenti(unittest.TestCase):
    def setUp(self):
        self.controller = ControllerListaAbbonamenti()

    def test_crea_lista(self):
        # Controlliamo che le due liste abbiano lo stesso numero di oggetti all'interno
        self.controller.get_lista_abbonamenti()
        self.assertTrue(os.path.exists("listaabbonamenti/data/lista_abbonamenti_salvata.pickle"))

        with open("listaabbonamenti/data/lista_abbonamenti_salvata.pickle", "rb") as handle:
            lista_abbonamenti = pickle.load(handle)
            self.assertEqual(len(self.controller.get_lista_abbonamenti()), len(lista_abbonamenti))

            # Verifico che ogni singolo elemento corrisponde tra le due liste
        for abbonamento1, abbonamento2 in zip(self.controller.get_lista_abbonamenti(), lista_abbonamenti):
            self.assertEqual(abbonamento1.codice, abbonamento2.codice)
            # Verifico che tutti gli attributi corrispondano tra i due oggetti
            for attr in abbonamento1.__dict__:
                self.assertEqual(getattr(abbonamento1, attr), getattr(abbonamento2, attr))

    def test_aggiunta_abbonamento(self):
        # Aggiungi un abbonamento al controller
        nuovo_abbonamento = Abbonamenti("codice123", "mensile", 20, 30)
        self.controller.aggiungi_abbonamenti(nuovo_abbonamento)

        # Controlla che l'abbonamento sia stato aggiunto correttamente
        lista_abbonamenti = self.controller.get_lista_abbonamenti()
        self.assertIn(nuovo_abbonamento, lista_abbonamenti)

    def test_eliminazione_abbonamento(self):
        # Aggiungi un abbonamento da eliminare
        abbonamento_da_eliminare = Abbonamenti("codice456", "annuale", 200, 365)
        self.controller.aggiungi_abbonamenti(abbonamento_da_eliminare)
        # Elimina l'abbonamento
        self.controller.rimuoviAbbonamento("codice456")
        # Controlla che l'abbonamento sia stato eliminato correttamente
        lista_abbonamenti = self.controller.get_lista_abbonamenti()

        self.assertNotIn(abbonamento_da_eliminare, lista_abbonamenti)


    def test_modifica_abbonamento(self):
        abbonamento_da_modificare = Abbonamenti("codice789", "settimanale", 50, 7)
        self.controller.aggiungi_abbonamenti(abbonamento_da_modificare)

        nuovo_costo = 60
        nuova_durata = 10
        self.controller.setInfoAbbonamento(abbonamento_da_modificare, nuovo_costo, nuova_durata)

        lista_abbonamenti = self.controller.get_lista_abbonamenti()
        self.assertIn(abbonamento_da_modificare, lista_abbonamenti)
        self.assertEqual(abbonamento_da_modificare.costo, nuovo_costo)
        self.assertEqual(abbonamento_da_modificare.durata, nuova_durata)

    def test_get_codice(self):
        abbonamento = Abbonamenti("codice001", "annuale", 120, 365)
        self.assertEqual(self.controller.getCodice(abbonamento), "codice001")

    def test_get_costo(self):
        abbonamento = Abbonamenti("codice002", "mensile", 30, 30)
        self.assertEqual(self.controller.getCosto(abbonamento), 30)

    def test_get_durata(self):
        abbonamento = Abbonamenti("codice003", "settimanale", 10, 7)
        self.assertEqual(self.controller.getDurata(abbonamento), 7)
if __name__ == '__main__':
    unittest.main()







