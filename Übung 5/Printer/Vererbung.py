# print_helper.py muss im gleichen Verzeichnis vorhanden sein
from print_helper import print_color, print_on_page

# Basisklasse Drucker
class Drucker:
    def __init__(self):
        self.page = None

    def set_page(self, page):
        self.page = page

# Klasse Page
class Page:
    def __init__(self, text, color):
        valid_colors = ['white', 'black', 'red', 'blue', 'green', 'yellow']
        assert color in valid_colors, f"{color} is not a valid color"
        self.text = text
        self.color = color

# Spezifische Drucker-Klassen
class SchwarzWeissDrucker(Drucker):
    def print_page(self):
        if self.page is not None:
            print(self.page.text)
        else:
            print("Keine Seite zum Drucken festgelegt.")

class FarbDrucker(Drucker):
    def print_page(self):
        if self.page is not None:
            print_color(self.page.text, self.page.color)
        else:
            print("Keine Seite zum Drucken festgelegt.")

class BildDrucker(Drucker):
    def __init__(self, folder):
        super().__init__()
        self.folder = folder

    def print_page(self):
        if self.page is not None:
            for letter in self.page.text:
                print_on_page(letter, self.page.color, self.folder)
        else:
            print("Keine Seite zum Drucken festgelegt.")

# Testlauf
if __name__ == "__main__":
    page = Page("Blaue Welt", "blue")
    sw_drucker = SchwarzWeissDrucker()
    farb_drucker = FarbDrucker()
    bild_drucker = BildDrucker("bilder")

    sw_drucker.set_page(page)
    sw_drucker.print_page()

    farb_drucker.set_page(page)
    farb_drucker.print_page()

    bild_drucker.set_page(page)
    bild_drucker.print_page()

    print("Testlauf mit Vererbung abgeschlossen.")
