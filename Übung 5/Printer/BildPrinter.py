from print_helper import print_on_page

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
