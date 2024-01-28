telefonbuch = {
    'Max Mustermann': '123-456789',
    'Eva Beispiel': '987-654321',
    'Anna Musterfrau': '555-123456',
    'Peter Test': '789-456123',
    'Lisa Probe': '321-654987'
}

while True:
    eingabe = input("Gib einen Namen ein (oder 'Enter' zum Beenden): ")

    # Überprüfe, ob der Benutzer "Enter" eingegeben hat
    if eingabe.lower() == 'enter':
        break  # Beende die Schleife, wenn "Enter" eingegeben wurde

    # Überprüfe, ob der eingegebene Name im Telefonbuch ist
    if eingabe in telefonbuch:
        telefonnummer = telefonbuch[eingabe]
        print(f"Die Telefonnummer von {eingabe} ist: {telefonnummer}")
    else:
        print(f"Der Name {eingabe} ist nicht im Telefonbuch.")

# Hier gelangt der Code hin, nachdem die Schleife beendet wurde
print("Programm beendet.")
