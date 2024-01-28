class Konto:
    def __init__(self, name):
        self.name = name
        self.kontostand = 0

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            print(f"{betrag} EUR wurden auf das Konto von {self.name} eingezahlt. Neuer Kontostand: {self.kontostand} EUR")
        else:
            print("Ungültiger Betrag für Einzahlung.")

    def auszahlen(self, betrag):
        if betrag > 0 and betrag <= self.kontostand:
            self.kontostand -= betrag
            print(f"{betrag} EUR wurden vom Konto von {self.name} abgehoben. Neuer Kontostand: {self.kontostand} EUR")
        else:
            print(f"Ungültiger Betrag für Auszahlung oder nicht ausreichend Geld auf dem Konto von {self.name}. Kontostand bleibt unverändert: {self.kontostand} EUR")

    def __str__(self):
        return f"Name: {self.name}, Kontostand: {self.kontostand} EUR"

# Beispiel-Nutzung:
donalds_konto = Konto("Donald Duck")
donalds_konto.einzahlen(100)
donalds_konto.einzahlen(50)
donalds_konto.auszahlen(30)
donalds_konto.auszahlen(80)

# Kontostand ausgeben
print(donalds_konto)
