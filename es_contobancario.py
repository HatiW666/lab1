# Esercizio: Creazione di una classe per un conto bancario
#
# Obiettivo: Creare una classe Python che rappresenti un conto bancario con le sue funzionalità di base.
#
# Descrizione:
#
# La classe ContoBancario dovrebbe avere i seguenti attributi:
#
#
# Intestatario: Nome e cognome del titolare del conto (stringa).
# Saldo: Saldo corrente del conto (float).
#
# Dovrebbe inoltre avere i seguenti metodi:
#
# deposito(importo): Aumenta il saldo del conto di un importo specificato.
# prelievo(importo): Diminuisce il saldo del conto di un importo specificato, verificando che il prelievo non superi il saldo disponibile.
# restituiscoSaldo(): Restituisce il valore del saldo corrente

class conto_bancario:
    def __init__(self, intestatario, saldo):
        self.intestatario = intestatario
        self.saldo = round(float(saldo), 2)

    def stampa_dati(self):
        print("Intestatario: ", self.intestatario)
        print("Saldo: ", self.saldo)

    def deposito(self):
        ricarica = round(float(input("Inserisci importo da ricaricare: ")), 2)
        self.saldo = round((self.saldo + ricarica),2)
        print(f"Operazione avvenuta con successo. Il tuo nuovo saldo è {self.saldo}")
        return conto_bancario(self.intestatario, self.saldo)

    def prelievo(self):
        prelievo =round(float(input("Inserisci importo da prelevare: ")), 2)
        self.saldo = round((self.saldo - prelievo),2)
        print(f"Operazione avvenuta con successo. Il tuo nuovo saldo è {self.saldo}")
        return conto_bancario(self.intestatario, self.saldo)


conto1 = conto_bancario("Mario Rossi", 666.666)
conto1.stampa_dati()

# conto1.deposito().stampa_dati()
conto1.prelievo().stampa_dati()
