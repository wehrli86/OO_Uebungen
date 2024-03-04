# Zuerst importieren wir die benötigten Klassen und Funktionen
from print_helper import print_color, print_on_page
from PIL import Image, ImageDraw, ImageFont
import os

# Definition der Page Klasse
class Page:
    def __init__(self, text, color):
        valid_colors = ['white', 'black', 'red', 'blue', 'green', 'yellow']
        assert color in valid_colors, f"{color} is not a valid color"
        self.text = text
        self.color = color

# Definition der Drucker Klassen
class SchwarzWeissDrucker:
    def __init__(self):
        self.page = None

    def set_page(self, page):
        self.page = page

    def print_page(self):
        if self.page is not None:
            print(self.page.text)
        else:
            print("Keine Seite zum Drucken festgelegt.")

class FarbDrucker:
    def __init__(self):
        self.page = None

    def set_page(self, page):
        self.page = page

    def print_page(self):
        if self.page is not None:
            print_color(self.page.text, self.page.color)
        else:
            print("Keine Seite zum Drucken festgelegt.")

class BildDrucker:
    def __init__(self, folder):
        self.page = None
        self.folder = folder

    def set_page(self, page):
        self.page = page

    def print_page(self):
        if self.page is not None:
            for letter in self.page.text:
                print_on_page(letter, self.page.color, self.folder)
        else:
            print("Keine Seite zum Drucken festgelegt.")

# Erstellen von Beispielseiten und Druckern
page = Page("Blaue Welt", "blue")
sw_drucker = SchwarzWeissDrucker()
farb_drucker = FarbDrucker()
bild_drucker = BildDrucker("bilder")

# Test der Drucker
sw_drucker.set_page(page)
sw_drucker.print_page()

farb_drucker.set_page(page)
farb_drucker.print_page()

bild_drucker.set_page(page)
bild_drucker.print_page()

print("Testlauf abgeschlossen.")
