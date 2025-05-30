class Videogioco:
    def __init__(self, id_gioco, nome, piattaforma, anno, genere, publisher, vendite):
        self.id = int(id_gioco)
        self.nome = nome
        self.piattaforma = piattaforma
        self.anno = anno
        self.genere = genere
        self.publisher = publisher
        self.vendite = vendite


    def __str__(self):
        return f"{self.id} | {self.nome} | {self.piattaforma} | {self.genere}"

    def __repr__(self):
        return f"{self.id} | {self.nome} | {self.piattaforma} | {self.genere}"

    def is_successful(self):
        return self.vendite["Global_Sales"] > 30

class Videoteca:
    def __init__(self, nome):
        self.nome = nome
        self.inventario = []
        self.id_presenti = []

    def stampa_catalogo(self):
        print(f"Catalogo {self.nome}: ")
        for g in self.inventario:
            print(g)


    def aggiungi_videogioco(self, vg):
        # trovato = False
        # for g in self.inventario:
        #     if vg.id == g.id :
        #         trovato = True
        #         break
        if vg.id in self.id_presenti:
            print(f"\"{vg.nome}\" già presente nel catalogo {self.nome}.")
        else:
            self.inventario.append(vg)
            self.id_presenti.append(vg.id)
            print(f"\"{vg.nome}\" aggiunto al catalogo {self.nome}!")

    def cerca_per_titolo(self, titolo):
        giochi_trovati = []
        for g in self.inventario:
            if titolo.lower() in g.nome.lower():
                giochi_trovati.append(g)
        return giochi_trovati

    def importa_csv(self, percorso):
        import csv
        from csv import DictReader
        with open(percorso, "r", encoding="utf-8") as f:
            lettura = csv.DictReader(f, delimiter=',')
            for riga in lettura:
                id = riga["Rank"]
                nome = riga["Name"]
                piattaforma = riga ["Platform"]
                anno_pubblicazione = riga["Year"]
                genere = riga["Genre"]
                sviluppatore = riga["Publisher"]
                diz_vendite = {"NA_Sales" : riga["NA_Sales"], "EU_Sales" : riga["EU_Sales"], "JP_Sales" : riga["JP_Sales"],"Other_Sales" : riga["Other_Sales"], "Global_Sales" : riga["Global_Sales"]}
                v = Videogioco(id, nome, piattaforma, anno_pubblicazione, genere, sviluppatore, diz_vendite)
                self.aggiungi_videogioco(v)

    #
    # def rimuovi_videogioco(self, vg):
    #     self.inventario.remove(vg)


if __name__ == '__main__':
    # diz_vendite = {"NA_Sales" : 10, "EU_Sales" : 20, "JP_Sales" : 31 ,"Other_Sales" : 20, "Global_Sales" : 82}
    # v1 = Videogioco(1, "Dredge of Pokemon", "PS", 2567, "Sport", "CLAITA", diz_vendite)
    # v2 = Videogioco(2, "Dredge of Infamy", "PS", 2567, "Sport", "CLAITA", diz_vendite)
    # v3 = Videogioco(3, "Dredge of Pokemon 2", "PS", 2567, "Sport", "CLAITA", diz_vendite)
    # vt1 = Videoteca("Gamestop")
    #
    # vt1.aggiungi_videogioco(v1)
    # vt1.aggiungi_videogioco(v2)
    # vt1.aggiungi_videogioco(v3)
    # vt1.aggiungi_videogioco(v3)
    # vt1.stampa_catalogo()
    # print(vt1.cerca_per_titolo("pokemon"))

    videoteca2 = Videoteca("Amazon")
    videoteca2.importa_csv("vgsales.csv")
    videoteca2.stampa_catalogo()
    gioco_da_cercare = input("Quale gioco vuoi cercare? ")
    print(videoteca2.cerca_per_titolo(gioco_da_cercare))