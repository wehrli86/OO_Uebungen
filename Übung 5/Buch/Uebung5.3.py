# Zuerst müssen wir die Klassen Buch und Bibliothek definieren, wie oben beschrieben.

# Klasse Buch
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
                print("Sie haben bereits das Ende des Buches erreicht.")
                self.schliessen()

# Klasse Bibliothek
class Bibliothek:
    def __init__(self):
        self.buchbestand = []
        self.ausgeliehene_buecher = []

    def buch_aufnehmen(self, buch):
        self.buchbestand.append(buch)
        print(f"Buch '{buch.titel}' wurde dem Bestand hinzugefügt.")

    def buch_ausleihen(self, buch):
        if buch in self.ausgeliehene_buecher:
            print(f"Buch '{buch.titel}' ist bereits ausgeliehen.")
        elif buch in self.buchbestand:
            self.buchbestand.remove(buch)
            self.ausgeliehene_buecher.append(buch)
            print(f"Buch '{buch.titel}' wurde ausgeliehen.")
        else:
            print(f"Buch '{buch.titel}' ist nicht im Bestand.")

    def buch_zurueckgeben(self, buch):
        if buch in self.ausgeliehene_buecher:
            self.ausgeliehene_buecher.remove(buch)
            self.buchbestand.append(buch)
            print(f"Buch '{buch.titel}' wurde zurückgegeben.")
        else:
            print(f"Buch '{buch.titel}' war nicht ausgeliehen.")

    def __str__(self):
        bestands_titel = ", ".join(buch.titel for buch in self.buchbestand)
        ausgeliehene_titel = ", ".join(buch.titel for buch in self.ausgeliehene_buecher)
        return f"Bücher im Bestand: {bestands_titel}\nAusgeliehene Bücher: {ausgeliehene_titel}"

# Testlauf
if __name__ == "__main__":
    # Erstellen einiger Bücher
    buch1 = Buch("Python Programmierung", "Max Mustermann", "Hardcover", "Informatik", ["Seite 1 Inhalt", "Seite 2 Inhalt"])
    buch2 = Buch("Das Leben des Pi", "Yann Martel", "Paperback", "Abenteuer", ["Seite 1 Inhalt", "Seite 2 Inhalt"])
    buch3 = Buch("Der Große Gatsby", "F. Scott Fitzgerald", "Hardcover", "Klassiker", ["Seite 1 Inhalt", "Seite 2 Inhalt"])

    # Erstellen der Bibliothek und Hinzufügen der Bücher
    bibliothek = Bibliothek()
    bibliothek.buch_aufnehmen(buch1)
    bibliothek.buch_aufnehmen(buch2)
    bibliothek.buch_aufnehmen(buch3)

    # Ausleihen und Zurückgeben von Büchern
    bibliothek.buch_ausleihen(buch1)
    bibliothek.buch_ausleihen(buch1)  # Versuch, ein bereits ausgeliehenes Buch auszuleihen
    bibliothek.buch_zurueckgeben(buch1)
    bibliothek.buch_zurueckgeben(buch1)  # Versuch, ein bereits zurückgegebenes Buch zurückzugeben

    # Demonstration des Lesens eines Buches
    buch1.oeffnen()
    buch1.lesen()
    buch1.lesen()
    buch1.schliessen()
    buch1.lesen()  # Versuch zu lesen, nachdem das Buch geschlossen wurde

    # Anzeigen des aktuellen Bibliotheksbestands und der ausgeliehenen Bücher
    print(bibliothek)
