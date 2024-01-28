def paare_bis_null(zahl):
    result_list = []
    for i in range(zahl, -1, -1):
        result_list.extend([-i, i])
    return result_list

# Benutzereingabe mit Fehlerüberprüfung
while True:
    try:
        eingabe_zahl = int(input("Bitte gib eine Zahl ein: "))
        break  # Beende die Schleife, wenn die Eingabe erfolgreich in eine Zahl umgewandelt wurde
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")

# Aufruf der Funktion und Ausgabe der Liste
ergebnis_liste = paare_bis_null(eingabe_zahl)
print("Paare von -", eingabe_zahl, "bis Null:", ergebnis_liste)
