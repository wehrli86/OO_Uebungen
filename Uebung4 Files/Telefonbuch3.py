telefonbuch = {
    'Max Mustermann': '123-456789',
    'Eva Beispiel': '987-654321',
    'Anna Musterfrau': '555-123456',
    'Peter Test': '789-456123',
    'Lisa Probe': '321-654987'
}

def telefonnummer_modus():
    eingabe = input("Gib einen Namen ein: ")
    telefonnummer = telefonbuch.get(eingabe, "Der Name ist nicht im Telefonbuch.")
    print(f"Die Telefonnummer von {eingabe} ist: {telefonnummer}")

def loesch_modus():
    eingabe = input("Gib den Namen ein, der gelöscht werden soll: ")
    if eingabe in telefonbuch:
        del telefonbuch[eingabe]
        print(f"Der Eintrag für {eingabe} wurde gelöscht.")
    else:
        print(f"Der Name {eingabe} ist nicht im Telefonbuch.")

def aendern_modus():
    eingabe_name = input("Gib den Namen ein: ")
    eingabe_telefonnummer = input("Gib die neue Telefonnummer ein: ")
    telefonbuch[eingabe_name] = eingabe_telefonnummer
    print(f"Der Eintrag für {eingabe_name} wurde geändert.")

def such_modus():
    eingabe = input("Gib einen Buchstaben ein: ")
    gefunden = False
    for name, telefonnummer in telefonbuch.items():
        if eingabe.lower() in name.lower():
            print(f"{name}: {telefonnummer}")
            gefunden = True
    if not gefunden:
        print(f"Keine Einträge gefunden, die den Buchstaben '{eingabe}' enthalten.")

while True:
    print("\nWähle einen Modus:")
    print("t - Telefonnummer-Modus")
    print("l - Lösch-Modus")
    print("a - Ändern-Modus")
    print("? - Such-Modus")
    print("Enter - Beenden")

    modus = input("Gib einen Buchstaben ein: ")

    if modus.lower() == 'enter':
        break

    if modus.lower() == 't':
        telefonnummer_modus()
    elif modus.lower() == 'l':
        loesch_modus()
    elif modus.lower() == 'a':
        aendern_modus()
    elif modus.lower() == '?':
        such_modus()
    else:
        print("Ungültige Eingabe. Bitte wähle einen der Buchstaben t, l, a, ? oder 'Enter' zum Beenden.")

