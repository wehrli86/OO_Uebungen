def berechne(zahl1, zahl2, operator):
    """
    Die Funktion berechne führt eine Rechnung basierend auf den gegebenen Zahlen und dem Operator durch.
    """
    if operator == "+":
        return zahl1 + zahl2
    elif operator == "-":
        return zahl1 - zahl2
    elif operator == "*":
        return zahl1 * zahl2
    elif operator == "/":
        if zahl2 != 0:
            return zahl1 / zahl2
        else:
            print("Division durch 0 ist nicht erlaubt.")
            exit()  # Programm beenden, da eine Division durch 0 versucht wurde
    else:
        print("Ungültiger Operator. Bitte nur +, -, *, oder / eingeben.")
        exit()  # Programm beenden, da ein ungültiger Operator eingegeben wurde

# Eingabe der ersten Zahl
zahl1 = float(input("Gib die erste Zahl ein: "))

# Eingabe des Operators (+, -, *, /)
operator = input("Gib +, -, *, oder / ein: ")

# Eingabe der zweiten Zahl
zahl2 = float(input("Gib die zweite Zahl ein: "))

# Aufruf der Funktion berechne und Ausgabe des Ergebnisses
ergebnis = berechne(zahl1, zahl2, operator)
print(f"{zahl1} {operator} {zahl2} = {ergebnis}")

