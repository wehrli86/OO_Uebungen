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

# Überprüfe, ob Rennen eingegeben wurden
if not distanzen:
    print("Keine Rennen eingegeben.")
else:
    # Gib die Gesamtanzahl der Rennen aus
    anzahl_rennen = len(distanzen)
    print("Anzahl der eingegebenen Rennen:", anzahl_rennen)

    # Gib die kürzeste und längste Distanz aus
    kuerzeste_distanz = min(distanzen)
    laengste_distanz = max(distanzen)
    print("Kürzeste Distanz:", kuerzeste_distanz)
    print("Längste Distanz:", laengste_distanz)

    # Gib die Gesamtdistanz und die durchschnittliche Distanz aus
    gesamtdistanz = sum(distanzen)
    durchschnitt_distanz = gesamtdistanz / anzahl_rennen
    print("Gesamtdistanz aller Rennen:", gesamtdistanz)
    print("Durchschnittliche Distanz:", durchschnitt_distanz)
