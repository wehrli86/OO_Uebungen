# Initialisiere eine leere Liste, um die eingegebenen Distanzen zu speichern
distanzen = []

# Verwende eine while-Schleife, um Distanzen einzulesen, bis der Benutzer nichts eingibt
while True:
    # Lies die Eingabe des Benutzers ein
    eingabe = input("Gib eine Distanz ein (oder drücke Enter zum Beenden): ")

    # Überprüfe, ob die Eingabe leer ist (Enter wurde gedrückt)
    if eingabe == "":
        break  # Beende die Schleife, wenn Enter gedrückt wurde

    try:
        # Versuche, die Eingabe in eine Zahl umzuwandeln und füge sie der Liste hinzu
        distanz = float(eingabe)
        distanzen.append(distanz)
        print("Eingegebene Distanz:", distanz)
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")

# Gib die gesamte Liste der eingegebenen Distanzen aus
print("Eingegebene Distanzen:", distanzen)
