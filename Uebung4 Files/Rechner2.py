# Eingabe der ersten Zahl
zahl1 = float(input("Gib die erste Zahl ein: "))  # Beachte die Umwandlung in eine Gleitkommazahl

# Eingabe des Operators (+ oder -)
operator = input("Gib + oder - ein: ")

# Eingabe der zweiten Zahl
zahl2 = float(input("Gib die zweite Zahl ein: "))  # Beachte die Umwandlung in eine Gleitkommazahl

# Initialisierung der Variable für das Ergebnis
ergebnis = 0

# Überprüfung des Operators und Berechnung des Ergebnisses
if operator == "+":
    ergebnis = zahl1 + zahl2
elif operator == "-":
    ergebnis = zahl1 - zahl2
else:
    print("Ungültiger Operator. Bitte nur + oder - eingeben.")
    exit()  # Programm beenden, da ein ungültiger Operator eingegeben wurde

# Ausgabe der Rechnung und des Ergebnisses
print(f"{zahl1} {operator} {zahl2} = {ergebnis}")
