# 1. Gestore di Prodotti:
# Crea una classe Prodotto con attributi come id, nome, prezzo, quantità e categoria.
# Crea una classe Magazzino che utilizza la classe Prodotto per gestire l'inventario.
# Implementa funzionalità per l'aggiunta di prodotti al magazzino, la rimozione,
# e la ricerca del prodotto e visualizzazione dell'elenco dei prodotti.
# Esempio di utilizzo
# # Crea un gestore di prodotti
# gestore_prodotti = GestoreProdotti()
# # Crea alcuni prodotti
# prodotto1 = Prodotto(101, "Maglietta", 15.90, 20, "Abbigliamento")
# prodotto2 = Prodotto(202, "Smartphone", 499.00, 15, "Elettronica")
# prodotto3 = Prodotto(303, "Scarpe da ginnastica", 59.90, 32, "Abbigliamento")
#
# # Aggiungi i prodotti al catalogo
# gestore_prodotti.aggiungi_prodotto(prodotto1)
# gestore_prodotti.aggiungi_prodotto(prodotto2)
# gestore_prodotti.aggiungi_prodotto(prodotto3)
#
# # Visualizza il catalogo
# gestore_prodotti.visualizza_catalogo()
#
# # Cerca un prodotto per nome
# prodotti_trovati = gestore_prodotti.cerca_prodotto("Maglietta")
# print(f"\nProdotti trovati per 'Maglietta':")
# for prodotto in prodotti_trovati:
#   print(prodotto)
#
# # Rimuovi un prodotto
# gestore_prodotti.rimuovi_prodotto(303)
#
# # Visualizza il catalogo aggiornato
# gestore_prodotti.visualizza_catalogo()


class Prodotto:
    def __init__(self, id, nome, prezzo, quantita, categoria):
        self.id = int(id)
        self.nome = nome
        self.prezzo = round(float(prezzo) ,2)
        self.quantita = int(quantita)
        self.categoria = categoria

def stampa_dati(self):
    print("id: ", self.id)
    print("nome: ", self.nome)
    print("prezzo: ", self.prezzo)
    print("quantita: ", self.quantita)
    print("categoria: ", self.categoria)


prodotto1 = Prodotto(101, "Maglietta", 15.90, 20, "Abbigliamento",)
prodotto2 = Prodotto(202, "Smartphone", 499.00, 15, "Elettronica",)
prodotto3 = Prodotto(303, "Scarpe da ginnastica", 59.90, 32, "Abbigliamento")

class Magazzino:
    def __init__(self, nome, iventario):
        self.nome = nome
        self.capienza = capienza
        self.inventario = []

magazzino1 = Magazzino("magazzino1")
    def aggiungi_prodotto_magazzino(self, prod):
        self.inventario.append(prod)


    # def si_puo_aggiungere(self):
    #     if len(self.inventario) < self.capienza:
    #         return True
    #     else:
    #         return False
Magazzino.aggiungi_prodotto_magazzino(prodotto1)

stampa_dati(prodotto1)
