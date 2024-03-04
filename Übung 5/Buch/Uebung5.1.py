class Buch:
    def __init__(self, titel, autor, einband, genre, seiten):
        self.titel = titel
        self.autor = autor
        self.einband = einband
        self.genre = genre
        self.seiten = seiten
        self.geoeffnet = False
        self.aktuelle_seite = 0

    def __str__(self):
        zustand = "geöffnet" if self.geoeffnet else "geschlossen"
        lesefortschritt = f", gelesen bis Seite {self.aktuelle_seite}" if self.geoeffnet and self.aktuelle_seite > 0 else ""
        return f"Buchtitel: {self.titel}, Autor: {self.autor}, Einband: {self.einband}, Genre: {self.genre}, Zustand: {zustand}{lesefortschritt}."

    def oeffnen(self):
        if self.geoeffnet:
            print("Das Buch ist bereits geöffnet.")
        else:
            self.geoeffnet = True
            self.aktuelle_seite = 0
            print(f"Das Buch '{self.titel}' wurde geöffnet.")

    def schliessen(self):
        if not self.geoeffnet:
            print("Das Buch ist bereits geschlossen.")
        else:
            self.geoeffnet = False
            print(f"Das Buch '{self.titel}' wurde geschlossen.")

    def lesen(self):
        if not self.geoeffnet:
            print("Das Buch muss zuerst geöffnet werden.")
        else:
            if self.aktuelle_seite < len(self.seiten):
                print(self.seiten[self.aktuelle_seite])
                self.aktuelle_seite += 1
                if self.aktuelle_seite == len(self.seiten):
                    print("Das war die letzte Seite. Das Buch wird automatisch geschlossen.")
                    self.schliessen()
            else:
                print("Das Buch wurde bereits bis zum Ende gelesen und wird geschlossen.")
                self.schliessen()