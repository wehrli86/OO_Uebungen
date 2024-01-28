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
def summe_der_liste(liste):
    summe = 0
    for zahl in liste:
        summe += zahl
    return summe

# Beispiel: Verwendung der Funktion paare_bis_null
eingabe_zahl = 3  # Hier sollte die zuvor eingegebene Zahl verwendet werden
ergebnis_liste = paare_bis_null(eingabe_zahl)

# Berechnung der Summe und Ausgabe
gesamte_summe = summe_der_liste(ergebnis_liste)
print("Summe der Liste:", gesamte_summe)
