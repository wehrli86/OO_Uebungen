from print_helper import print_color

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
