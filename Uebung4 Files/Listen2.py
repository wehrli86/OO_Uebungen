def eingabe_bis_null(zahl):
    return list(range(zahl, -1, -1))

# Benutzereingabe mit Fehlerüberprüfung
while True:
    try:
        eingabe_zahl = int(input("Bitte gib eine Zahl ein: "))
        break  # Beende die Schleife, wenn die Eingabe erfolgreich in eine Zahl umgewandelt wurde
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")

# Aufruf der Funktion und Ausgabe der Liste
ergebnis_liste = eingabe_bis_null(eingabe_zahl)
print("Liste von", eingabe_zahl, "bis Null:", ergebnis_liste)
