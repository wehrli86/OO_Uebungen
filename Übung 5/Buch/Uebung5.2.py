class Bibliothek:
    def __init__(self):
        self.buchbestand = []
        self.ausgeliehene_buecher = []

    def buch_aufnehmen(self, buch):
        if buch not in self.buchbestand and buch not in self.ausgeliehene_buecher:
            self.buchbestand.append(buch)
            print(f"Buch '{buch.titel}' wurde dem Bestand hinzugefügt.")
        else:
            print(f"Buch '{buch.titel}' befindet sich bereits im Bestand.")

    def buch_ausleihen(self, buch):
        if buch in self.ausgeliehene_buecher:
            print(f"Buch '{buch.titel}' ist bereits ausgeliehen.")
        elif buch in self.buchbestand:
            self.buchbestand.remove(buch)
            self.ausgeliehene_buecher.append(buch)
            print(f"Buch '{buch.titel}' wurde ausgeliehen.")
        else:
            print(f"Buch '{buch.titel}' befindet sich nicht im Bestand.")

    def buch_zurueckgeben(self, buch):
        if buch in self.ausgeliehene_buecher:
            self.ausgeliehene_buecher.remove(buch)
            self.buchbestand.append(buch)
            print(f"Buch '{buch.titel}' wurde zurückgegeben und dem Bestand hinzugefügt.")
        else:
            print(f"Buch '{buch.titel}' wurde nicht ausgeliehen.")

    def __str__(self):
        bestands_titel = ", ".join(buch.titel for buch in self.buchbestand)
        ausgeliehene_titel = ", ".join(buch.titel for buch in self.ausgeliehene_buecher)
        return f"Bücher im Bestand: {bestands_titel}\nAusgeliehene Bücher: {ausgeliehene_titel}"
