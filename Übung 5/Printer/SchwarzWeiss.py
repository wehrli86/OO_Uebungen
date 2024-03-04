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
