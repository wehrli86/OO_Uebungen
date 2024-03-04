class Konto:
    def __init__(self, name):
        self.name = name
        self.kontostand = 0

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            print(f"{betrag} CHF wurden auf das Konto von {self.name} eingezahlt. Neuer Kontostand: {self.kontostand} CHF")
        else:
            print("Ungültiger Betrag für Einzahlung.")

    def auszahlen(self, betrag):
        if 0 < betrag <= self.kontostand:
            self.kontostand -= betrag
            print(f"{betrag} CHF wurden vom Konto von {self.name} abgehoben. Neuer Kontostand: {self.kontostand} CHF")
        else:
            print("Ungültiger Betrag für Auszahlung.")

# Beispiel-Nutzung:
donalds_konto = Konto("Donald Duck")
donalds_konto.einzahlen(100)
donalds_konto.auszahlen(30)
