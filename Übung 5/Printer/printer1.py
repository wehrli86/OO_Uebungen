class Page:
    def __init__(self, text, color):
        # Definierte gültige Farben
        valid_colors = ['white', 'black', 'red', 'blue', 'green', 'yellow']
        # Überprüft, ob die übergebene Farbe gültig ist
        assert color in valid_colors, f"{color} is not a valid color"
        
        self.text = text
        self.color = color

# Beispiel zur Verwendung der Page-Klasse
try:
    page = Page("Dies ist ein Beispieltext.", "blue")  # Gültige Farbe
    print(f"Seite erstellt mit Text: {page.text} in Farbe: {page.color}")
    
    invalid_page = Page("Dies ist der Errorcode.", "purple")  # Ungültige Farbe
except AssertionError as error:
    print(error)
