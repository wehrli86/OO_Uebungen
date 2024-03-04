def null_bis_eingabe(zahl):
    return list(range(zahl + 1))

# Benutzereingabe mit Fehlerüberprüfung
while True:
    try:
        eingabe_zahl = int(input("Bitte gib eine Zahl ein: "))
        break  # Beende die Schleife, wenn die Eingabe erfolgreich in eine Zahl umgewandelt wurde
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")

# Aufruf der Funktion und Ausgabe der Liste
ergebnis_liste = null_bis_eingabe(eingabe_zahl)
print("Liste von Null bis", eingabe_zahl, ":", ergebnis_liste)
