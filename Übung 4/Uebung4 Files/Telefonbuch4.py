import csv
import os

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

def speichern():
    try:
        with open("telefonbuch.csv", "w", newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for name, telefonnummer in telefonbuch.items():
                writer.writerow([name, telefonnummer])
        print("Telefonbuch erfolgreich gespeichert.")
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")

def oeffnen():
    try:
        telefonbuch.clear()  # Löscht bestehende Einträge, um die Datei zu laden
        if os.path.exists("telefonbuch.csv"):
            with open("telefonbuch.csv", newline='') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    if len(row) == 2:
                        name, telefonnummer = row
                        telefonbuch[name] = telefonnummer
            print("Telefonbuch erfolgreich geladen.")
        else:
            print("Die Datei existiert noch nicht. Es wurden keine Einträge geladen.")
    except Exception as e:
        print(f"Fehler beim Laden: {e}")

# Speichern und Öffnen beim Programmstart
speichern()
oeffnen()

while True:
    print("\nWähle einen Modus:")
    print("t - Telefonnummer-Modus")
    print("l - Lösch-Modus")
    print("a - Ändern-Modus")
    print("? - Such-Modus")

    # Optionen nur anzeigen, wenn bereits gespeichert und geladen wurde
    if telefonbuch:
        print("s - Speichern")
        print("o - Öffnen")

    print("Enter - Beenden")

    modus = input("Gib einen Buchstaben ein: ").lower()

    if modus == 't':
        telefonnummer_modus()
    elif modus == 'l':
        loesch_modus()
    elif modus == 'a':
        aendern_modus()
    elif modus == '?':
        such_modus()
    elif modus == 's':
        speichern()
    elif modus == 'o':
        oeffnen()
    elif not modus:
        break
    else:
        print("Ungültige Eingabe. Bitte wähle einen der Buchstaben t, l, a, ?, s, o oder drücke Enter zum Beenden.")
